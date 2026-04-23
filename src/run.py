from __future__ import annotations

import argparse
import csv
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from lxml import etree

from . import parse_gs, parse_gspp, report
from .discriminator import make_discriminator
from .judge import combine_matches, make_judge, preload_cache
from .models import Match
from .shortlist import make_shortlister
from . import visualize_graph
from .validation import validate_matches, print_validation_report
from .golden_dataset import evaluate_matches, print_evaluation_report

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANUAL_CSV = ROOT / "out" / "gspp_compliance_v3approach.csv"
_COVERAGE_SCORE = {"keine": 0, "teilweise": 1, "voll": 2}
_TESTING_ORIGIN_RE = re.compile(r"\[GS\+\+:\s*([^\]]+)\]")
_REQ_ID_RE = re.compile(r"^([A-Z]+(?:\.\d+)+\.A\d+)\s+")
_DOCBOOK_NS = {"d": "http://docbook.org/ns/docbook"}


def _normalize_coverage(raw: str | None) -> str:
    value = (raw or "").strip().lower()
    mapping = {
        "voll": "voll",
        "vollstandig": "voll",
        "vollstaendig": "voll",
        "vollständig": "voll",
        "teilweise": "teilweise",
        "partiell": "teilweise",
        "keine": "keine",
        "n/a": "keine",
        "na": "keine",
        "": "keine",
    }
    return mapping.get(value, "keine")


def _parse_models(raw_models: list[str] | str) -> list[str]:
    if isinstance(raw_models, str):
        raw_values = [raw_models]
    else:
        raw_values = raw_models

    models: list[str] = []
    for raw_value in raw_values:
        models.extend(model.strip() for model in raw_value.split(",") if model.strip())
    if not models:
        raise ValueError("--model must contain at least one model name")
    return models


def _safe_model_label(models: list[str]) -> str:
    return "+".join(models).replace("/", "_").replace(":", "_").replace(",", "_")


def _parse_manual_match(row: dict[str, str]) -> Match:
    gs_ids = [gs_id.strip() for gs_id in (row.get("gs_ids") or "").split(";") if gs_id.strip()]
    rationale = (row.get("rationale") or "").strip()
    gap_notes = (row.get("gap_notes") or "").strip() or None
    if rationale == "N/A":
        rationale = ""
    if gap_notes == "N/A":
        gap_notes = None
    return Match(
        gspp_id=(row.get("gspp_id") or "").strip(),
        gs_candidates=gs_ids,
        confidence=float(row.get("confidence") or 0.0),
        coverage=_normalize_coverage(row.get("coverage")),
        rationale=rationale,
        gap_notes=gap_notes,
    )


def _merge_manual_match(existing: Match, incoming: Match) -> Match:
    merged_ids = list(existing.gs_candidates)
    seen_ids = set(merged_ids)
    for gs_id in incoming.gs_candidates:
        if gs_id not in seen_ids:
            merged_ids.append(gs_id)
            seen_ids.add(gs_id)

    merged_coverage = (
        incoming.coverage
        if _COVERAGE_SCORE.get(incoming.coverage, 0) > _COVERAGE_SCORE.get(existing.coverage, 0)
        else existing.coverage
    )
    merged_confidence = max(existing.confidence, incoming.confidence)

    merged_rationale = existing.rationale
    if incoming.rationale and incoming.rationale not in merged_rationale:
        merged_rationale = (
            f"{existing.rationale}\n{incoming.rationale}".strip()
            if existing.rationale
            else incoming.rationale
        )

    merged_gap_notes = existing.gap_notes
    if incoming.gap_notes and incoming.gap_notes != existing.gap_notes:
        merged_gap_notes = (
            f"{existing.gap_notes}\n{incoming.gap_notes}".strip()
            if existing.gap_notes
            else incoming.gap_notes
        )

    return Match(
        gspp_id=existing.gspp_id,
        gs_candidates=merged_ids,
        confidence=merged_confidence,
        coverage=merged_coverage,
        rationale=merged_rationale,
        gap_notes=merged_gap_notes,
    )


def _load_manual_matches(csv_path: Path, allowed_ids: set[str]) -> dict[str, Match]:
    matches: dict[str, Match] = {}
    # utf-8-sig tolerates BOM-prefixed CSV exports (e.g. from Excel)
    # so the first header is parsed as "gspp_id" instead of "\ufeffgspp_id".
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            gspp_id = (row.get("gspp_id") or "").strip()
            if not gspp_id or gspp_id not in allowed_ids:
                continue
            current = _parse_manual_match(row)
            if gspp_id in matches:
                matches[gspp_id] = _merge_manual_match(matches[gspp_id], current)
            else:
                matches[gspp_id] = current
    return matches


def _load_testing_origin_map(xml_path: Path) -> dict[str, str]:
    """Load mapping fake requirement ID -> GS++ control ID from testing XML titles."""
    mapping: dict[str, str] = {}
    tree = etree.parse(str(xml_path))
    for title_node in tree.getroot().findall(".//d:section/d:title", _DOCBOOK_NS):
        title_text = "".join(title_node.itertext()).strip()
        req_match = _REQ_ID_RE.match(title_text)
        origin_match = _TESTING_ORIGIN_RE.search(title_text)
        if not req_match or not origin_match:
            continue
        fake_req_id = req_match.group(1).strip()
        origin_id = origin_match.group(1).strip()
        if fake_req_id and origin_id:
            mapping[fake_req_id] = origin_id
    return mapping


def _build_testing_truth_map(origin_map: dict[str, str]) -> dict[str, set[str]]:
    """Build gspp_id -> set(fake_gs_id) from fake_id -> gspp_id origin map."""
    truth: dict[str, set[str]] = {}
    for fake_id, origin in origin_map.items():
        truth.setdefault(origin, set()).add(fake_id)
    return truth


def _display_candidate_ids(ids: list[str], origin_map: dict[str, str] | None) -> list[str]:
    """Display GS candidate IDs, replacing FAKE IDs with originating GS++ IDs when available."""
    if not origin_map:
        return ids
    return [origin_map.get(gid, gid) for gid in ids]


def _is_same_or_hierarchical_id(left: str, right: str) -> bool:
    """Return True for exact match or parent/child relation on dot-separated IDs."""
    l = (left or "").strip()
    r = (right or "").strip()
    if not l or not r:
        return False
    return l == r or l.startswith(r + ".") or r.startswith(l + ".")


def _expand_with_hierarchical_candidates(
    selected_ids: list[str],
    shortlist_ids: list[str],
    origin_map: dict[str, str] | None,
) -> list[str]:
    """Expand selected candidates with hierarchical alternatives from shortlist.

    - In testing mode (origin_map provided): compare by mapped GS++ origin IDs.
    - In real mode (no origin_map): compare by candidate IDs directly.
    """
    if origin_map:
        selected_compare_ids = [origin_map[sid] for sid in selected_ids if sid in origin_map]
        if not selected_compare_ids:
            return selected_ids
    else:
        selected_compare_ids = list(selected_ids)
        if not selected_compare_ids:
            return selected_ids

    expanded = list(selected_ids)
    seen = set(expanded)
    for candidate_id in shortlist_ids:
        candidate_compare_id = origin_map.get(candidate_id) if origin_map else candidate_id
        if not candidate_compare_id:
            continue
        if any(
            _is_same_or_hierarchical_id(candidate_compare_id, selected_compare_id)
            for selected_compare_id in selected_compare_ids
        ):
            if candidate_id not in seen:
                expanded.append(candidate_id)
                seen.add(candidate_id)

    return expanded


def _calculate_confusion_counts(
    matches: list[Match],
    gspp_ids: list[str],
    gs_total: int,
    truth_map: dict[str, set[str]],
    discriminated_matches: list[tuple[Match, dict[str, tuple[str, str]]]] | None,
    origin_map: dict[str, str] | None = None,
    hierarchical_match: bool = False,
) -> tuple[int, int, int, int]:
    """Calculate aggregate TP/FP/FN/TN over all evaluated GS++ IDs."""
    predicted_by_gspp: dict[str, set[str]] = {}
    if discriminated_matches:
        for match, per_candidate in discriminated_matches:
            predicted_by_gspp[match.gspp_id] = {
                gid for gid, (decision, _) in per_candidate.items() if decision == "keep"
            }
    else:
        for match in matches:
            predicted_by_gspp[match.gspp_id] = set(match.gs_candidates)

    tp = fp = fn = tn = 0
    for gspp_id in gspp_ids:
        pred = predicted_by_gspp.get(gspp_id, set())
        truth = truth_map.get(gspp_id, set())
        if hierarchical_match and origin_map is not None:
            truth = {
                fake_id
                for fake_id, origin_id in origin_map.items()
                if _is_same_or_hierarchical_id(gspp_id, origin_id)
            }
        local_tp = len(pred & truth)
        local_fp = len(pred - truth)
        local_fn = len(truth - pred)
        local_tn = max(0, gs_total - local_tp - local_fp - local_fn)
        tp += local_tp
        fp += local_fp
        fn += local_fn
        tn += local_tn

    return tp, fp, fn, tn


def main(argv: list[str] | None = None) -> int:
    load_dotenv(ROOT / ".env")
    p = argparse.ArgumentParser(description="Map Grundschutz++ to IT-Grundschutz")
    p.add_argument("--model", nargs="+", default=["claude-sonnet-4-5"],
                   help="one or more models, either space-separated or comma-separated, e.g. --model claude-sonnet-4-5 gpt-5.4-mini")
    p.add_argument("--scope", default="",
                   help="GS++ ID-prefix to include (default: all categories)")
    p.add_argument("--sample-ratio", type=float, default=0.20,
                   help="ratio of GS++ controls sampled per category (default: 0.20 = 20%%, <=0 or >=1 means all)")
    p.add_argument("--seed", type=int, default=42,
                   help="random seed for per-category sampling")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument(
        "--expand-hierarchical",
        action="store_true",
        help="expand selected candidates with hierarchical parent/child alternatives from shortlist",
    )
    p.add_argument("--gs-levels", default="Basis,Standard,Hoch",
                   help="comma-separated levels from GS to consider (default: all)")
    p.add_argument("--limit", type=int, default=0, help="limit number of GS++ controls (0=all)")
    p.add_argument(
        "--testing-mode",
        action="store_true",
        help="run against a testing GS XML dataset and compute TP/FP/FN/TN metrics",
    )
    p.add_argument(
        "--testing-gs-xml",
        default=str(ROOT / "data" / "fake.xml"),
        help="GS XML path used in testing mode (default: data/fake.xml)",
    )
    p.add_argument(
        "--testing-limit",
        type=int,
        default=0,
        help="limit number of GS++ controls only for testing mode (0=all)",
    )
    p.add_argument(
        "--manual-csv",
        nargs="?",
        const=str(DEFAULT_MANUAL_CSV),
        default="",
        help=(
            "optional CSV with additional manual mappings to add after the model run; "
            "when passed without a path, defaults to out/gspp_compliance_v2.csv"
        ),
    )
    p.add_argument("--discriminator", action="store_true",
                   help="enable LLM-based discriminator to filter/validate mappings")
    p.add_argument("--discriminator-model", default="claude-sonnet-4-5",
                   help="model to use for discriminator (default: claude-sonnet-4-5)")
    p.add_argument("--discriminator-strict", action="store_true",
                   help="use aggressive discrimination (keep only essential candidates, max 3)")
    p.add_argument("--shortlist-method", default="tfidf",
                   choices=["tfidf", "embedding", "cached_embedding"],
                   help="method for retrieving GS candidates: tfidf (fast), embedding (better quality)")
    p.add_argument("--evaluate", action="store_true",
                   help="evaluate matches against golden dataset")
    p.add_argument("--out-dir", default=str(ROOT / "out"))
    p.add_argument("--concurrency", type=int, default=1,
                   help="parallel classify/discriminator requests (1=sequential)")
    args = p.parse_args(argv)

    models = _parse_models(args.model)
    model_sources = list(models)
    if args.testing_mode and args.gs_levels.strip() == "Basis,Standard":
        levels = ("Basis", "Standard", "Hoch")
    else:
        levels = tuple(s.strip() for s in args.gs_levels.split(",") if s.strip())
    gs_xml_path = Path(args.testing_gs_xml) if args.testing_mode else (ROOT / "data" / "gs.xml")
    effective_limit = args.testing_limit if args.testing_mode and args.testing_limit else args.limit
    scope_display = args.scope or "<all>"
    hierarchical_expansion_enabled = args.testing_mode or args.expand_hierarchical
    print(
        f"[i] scope={scope_display!r} sample_ratio={args.sample_ratio:.2f} "
        f"seed={args.seed} models={'+'.join(model_sources)} top_k={args.top_k} levels={levels} "
        f"shortlist={args.shortlist_method}",
        file=sys.stderr,
    )
    if args.testing_mode:
        print(f"[i] testing mode enabled: gs_dataset={gs_xml_path}", file=sys.stderr)
    if hierarchical_expansion_enabled and not args.testing_mode:
        print("[i] hierarchical expansion enabled", file=sys.stderr)

    if args.testing_mode:
        # Im Testmodus: Beide Seiten aus gspp.json laden (perfektes 1:1)
        gspp_reqs = parse_gspp.parse(
            ROOT / "data" / "gspp.json",
            scope_prefix=args.scope,
            sample_ratio_per_category=args.sample_ratio,
            random_seed=args.seed,
        )
        gs_reqs = parse_gspp.parse(
            ROOT / "data" / "gspp.json",
            scope_prefix=args.scope,
            sample_ratio_per_category=args.sample_ratio,
            random_seed=args.seed,
        )
    else:
        gspp_reqs = parse_gspp.parse(
            ROOT / "data" / "gspp.json",
            scope_prefix=args.scope,
            sample_ratio_per_category=args.sample_ratio,
            random_seed=args.seed,
        )
        gs_reqs = parse_gs.parse(gs_xml_path, levels=levels)
    if effective_limit:
        gspp_reqs = gspp_reqs[: effective_limit]
    print(f"[i] {len(gspp_reqs)} GS++ controls | {len(gs_reqs)} GS requirements", file=sys.stderr)
    print(f"[DEBUG] Loaded GS++ nodes: {len(gspp_reqs)}", file=sys.stderr)
    print(f"[DEBUG] Loaded GS nodes: {len(gs_reqs)}", file=sys.stderr)

    testing_origin_map: dict[str, str] | None = None
    if args.testing_mode:
        testing_origin_map = _load_testing_origin_map(gs_xml_path)
        print(f"[i] loaded {len(testing_origin_map)} testing origin markers", file=sys.stderr)

    gspp_idx = {r.id: r for r in gspp_reqs}
    gs_idx = {r.id: r for r in gs_reqs}

    manual_csv_path = Path(args.manual_csv) if args.manual_csv else None
    manual_source: str | None = None
    manual_matches: dict[str, Match] = {}
    if manual_csv_path and manual_csv_path.exists():
        manual_source = f"manual:{manual_csv_path.stem}"
        manual_matches = _load_manual_matches(manual_csv_path, set(gspp_idx))
        if manual_matches:
            model_sources.append(manual_source)
            print(f"[i] loaded manual mappings from {manual_csv_path} for {len(manual_matches)} GS++ controls", file=sys.stderr)

    # Im Testmodus: EmbeddingShortlister für beide Seiten mit GS++-Knoten initialisieren
    if args.testing_mode and args.shortlist_method in ("embedding", "cached_embedding"):
        sl = make_shortlister(gspp_reqs, method=args.shortlist_method)
    else:
        sl = make_shortlister(gs_reqs, method=args.shortlist_method)

    # Batch-encode all query embeddings now → top_k inside threaded loop = pure numpy.
    if hasattr(sl, "precompute_queries"):
        print(f"[i] precomputing query embeddings for {len(gspp_reqs)} GS++ items ...", file=sys.stderr)
        sl.precompute_queries(gspp_reqs)

    judges = [make_judge(model) for model in models]

    n_cached = preload_cache()
    if n_cached:
        print(f"[i] preloaded {n_cached} cached judge results into memory", file=sys.stderr)

    def _classify_one(i: int, q):
        cands = [r for r, _ in sl.top_k(q, k=args.top_k)]
        cand_ids = [c.id for c in cands]
        print(f"[{i}/{len(gspp_reqs)}] {q.id} ...", file=sys.stderr)
        parts = [judge.classify(q, cands) for judge in judges]
        part_names = [judge.model for judge in judges]
        if manual_source and q.id in manual_matches:
            parts.append(manual_matches[q.id])
            part_names.append(manual_source)
        m = combine_matches(parts, part_names) if len(parts) > 1 else parts[0]
        if hierarchical_expansion_enabled:
            m.gs_candidates = _expand_with_hierarchical_candidates(
                m.gs_candidates,
                cand_ids,
                testing_origin_map,
            )
        display_candidates = _display_candidate_ids(m.gs_candidates, testing_origin_map)
        print(f"    [{i}] → coverage={m.coverage} conf={m.confidence:.2f} gs={display_candidates}", file=sys.stderr)
        return i, m

    matches_by_idx: dict[int, Match] = {}
    if args.concurrency > 1:
        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = [ex.submit(_classify_one, i, q) for i, q in enumerate(gspp_reqs, 1)]
            for fut in as_completed(futures):
                i, m = fut.result()
                matches_by_idx[i] = m
    else:
        for i, q in enumerate(gspp_reqs, 1):
            i, m = _classify_one(i, q)
            matches_by_idx[i] = m
    matches = [matches_by_idx[i] for i in sorted(matches_by_idx)]
    model_label = "+".join(model_sources)

    # Validate matches
    print("[i] validating matches ...", file=sys.stderr)
    validation_issues = validate_matches(
        matches, gspp_idx, gs_idx, relax_id_check=args.testing_mode
    )
    error_count = sum(1 for issues in validation_issues.values() for i in issues if i.severity == "error")
    warning_count = sum(1 for issues in validation_issues.values() for i in issues if i.severity == "warning")
    print(f"[i] validation complete: {error_count} errors, {warning_count} warnings", file=sys.stderr)
    if error_count > 0:
        print_validation_report(validation_issues)

    # Optional: evaluate against golden dataset
    if args.evaluate:
        print("[i] evaluating against golden dataset ...", file=sys.stderr)
        eval_metrics = evaluate_matches(matches)
        print_evaluation_report(eval_metrics)

    # Optional: run discriminator to filter/validate matches
    discriminated_matches: list[tuple[Match, dict[str, tuple[str, str]]]] | None = None
    if args.discriminator:
        print(f"[i] running discriminator ({args.discriminator_model}) ...", file=sys.stderr)
        discriminator = make_discriminator(args.discriminator_model, strict=args.discriminator_strict)
        discriminated_matches = []
        def _discriminate_one(i: int, m: Match):
            gspp_req = gspp_idx.get(m.gspp_id)
            if not gspp_req:
                return i, None
            print(f"[{i}/{len(matches)}] discriminating {m.gspp_id} ...", file=sys.stderr)
            try:
                per_candidate = discriminator.decide(m, gspp_req, gs_idx)
                if args.discriminator_strict:
                    max_keep = 3
                    kept = [(gid, reason) for gid, (dec, reason) in per_candidate.items() if dec == "keep"]
                    if len(kept) > max_keep:
                        kept.sort(key=lambda x: len(x[1]), reverse=True)
                        to_remove = [gid for gid, _ in kept[max_keep:]]
                        for gid in to_remove:
                            per_candidate[gid] = ("remove", per_candidate[gid][1] + " [STRICT: removed due to limit]")
                accepted_ids = _display_candidate_ids(
                    [gid for gid, (dec, _) in per_candidate.items() if dec == "keep"],
                    testing_origin_map,
                )
                denied_ids = _display_candidate_ids(
                    [gid for gid, (dec, _) in per_candidate.items() if dec == "remove"],
                    testing_origin_map,
                )
                print(f"    [{i}] → accepted={accepted_ids} denied={denied_ids}", file=sys.stderr)
                return i, (m, per_candidate)
            except Exception as e:
                print(f"    [{i}] → error: {e}", file=sys.stderr)
                return i, (m, {gid: ("error", str(e)) for gid in m.gs_candidates})

        disc_results: dict[int, tuple[Match, dict[str, tuple[str, str]]]] = {}
        if args.concurrency > 1:
            with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
                futures = [ex.submit(_discriminate_one, i, m) for i, m in enumerate(matches, 1)]
                for fut in as_completed(futures):
                    i, res = fut.result()
                    if res is not None:
                        disc_results[i] = res
        else:
            for i, m in enumerate(matches, 1):
                i, res = _discriminate_one(i, m)
                if res is not None:
                    disc_results[i] = res
        discriminated_matches = [disc_results[i] for i in sorted(disc_results)]

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_model = _safe_model_label(model_sources)
    out_dir = Path(args.out_dir)
    csv_path = out_dir / f"mapping_{safe_model}_{ts}.csv"
    md_path = out_dir / f"mapping_{safe_model}_{ts}.md"
    report.write_csv(csv_path, matches, gspp_idx, gs_idx, model_label)
    report.write_markdown(md_path, matches, gspp_idx, gs_idx, model_label)
    print(f"[i] wrote {csv_path}\n[i] wrote {md_path}", file=sys.stderr)

    # Write discriminated results if available
    if discriminated_matches:
        disc_csv_path = out_dir / f"discriminated_{safe_model}_{args.discriminator_model}_{ts}.csv"
        report.write_discriminated_csv(
            disc_csv_path,
            discriminated_matches,
            gspp_idx,
            gs_idx,
            args.discriminator_model,
            model_label,
        )
        print(f"[i] wrote {disc_csv_path}", file=sys.stderr)
        
        # Print summary
        accepted = sum(
            1 for _, per_candidate in discriminated_matches
            for dec, _ in per_candidate.values() if dec == "keep"
        )
        denied = sum(
            1 for _, per_candidate in discriminated_matches
            for dec, _ in per_candidate.values() if dec == "remove"
        )
        errors = sum(
            1 for _, per_candidate in discriminated_matches
            for dec, _ in per_candidate.values() if dec == "error"
        )
        print(f"[i] discriminator results: {accepted} accepted, {denied} denied, {errors} errors (per candidate)", file=sys.stderr)
        
        # Generate visualization for discriminated results
        disc_viz_path = out_dir / f"discriminated_{safe_model}_{args.discriminator_model}_{ts}_graph.html"
        visualize_graph.visualize_discriminated(
            disc_viz_path,
            discriminated_matches,
            gspp_idx,
            gs_idx,
            title=f"GS++ → GS Mapping (Discriminated by {args.discriminator_model})",
        )
        print(f"[i] wrote {disc_viz_path}", file=sys.stderr)

    if args.testing_mode:
        # Im Testmodus: GS++ gegen GS++ vergleichen, IDs direkt vergleichen
        eval_ids = [r.id for r in gspp_reqs]
        # Wahrheit: Jede GS++-ID muss sich selbst finden
        truth_map = {gspp_id: {gspp_id} for gspp_id in eval_ids}
        tp, fp, fn, tn = _calculate_confusion_counts(
            matches,
            eval_ids,
            len(gs_reqs),
            truth_map,
            discriminated_matches,
            origin_map=None,
            hierarchical_match=False,
        )
        total = tp + fp + fn + tn
        precision = (tp / (tp + fp)) if (tp + fp) else 0.0
        recall = (tp / (tp + fn)) if (tp + fn) else 0.0
        accuracy = ((tp + tn) / total) if total else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0

        print(
            "[i] testing confusion matrix: "
            f"TP={tp} FP={fp} FN={fn} TN={tn} "
            f"| precision={precision:.4f} recall={recall:.4f} f1={f1:.4f} accuracy={accuracy:.4f}",
            file=sys.stderr,
        )

        metrics_path = out_dir / f"testing_metrics_{safe_model}_{ts}.csv"
        with metrics_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow([
                "timestamp",
                "testing_dataset",
                "gspp_evaluated",
                "gs_total",
                "truth_covered_gspp",
                "tp",
                "fp",
                "fn",
                "tn",
                "precision",
                "recall",
                "f1",
                "accuracy",
                "discriminator_enabled",
                "discriminator_model",
                "models",
            ])
            w.writerow([
                ts,
                str(gs_xml_path),
                len(eval_ids),
                len(gs_reqs),
                len(truth_map),
                tp,
                fp,
                fn,
                tn,
                f"{precision:.6f}",
                f"{recall:.6f}",
                f"{f1:.6f}",
                f"{accuracy:.6f}",
                bool(args.discriminator),
                args.discriminator_model if args.discriminator else "",
                model_label,
            ])
        print(f"[i] wrote {metrics_path}", file=sys.stderr)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
