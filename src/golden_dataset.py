"""Golden dataset of manually verified GS++ → GS mappings for evaluation.

These mappings have been reviewed by domain experts and represent
high-quality ground truth for evaluating the automated mapping system.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass
class GoldenMapping:
    """A verified mapping from GS++ to GS requirements."""
    gspp_id: str
    gspp_title: str
    gs_ids: list[str]
    coverage: Literal["voll", "teilweise", "keine"]
    confidence: float
    rationale: str
    notes: str | None = None


# Verified golden mappings
# These represent high-confidence ground truth from expert review
GOLDEN_MAPPINGS: list[GoldenMapping] = [
    # Governance und Compliance - ISMS Basis
    GoldenMapping(
        gspp_id="GC.6.1.1",
        gspp_title="Festlegung einer Sicherheitsstrategie",
        gs_ids=["ISMS.1.A2"],
        coverage="voll",
        confidence=0.95,
        rationale="ISMS.1.A2 deckt die Festlegung von Sicherheitszielen und -strategie durch die Leitung vollständig ab.",
    ),
    GoldenMapping(
        gspp_id="GC.6.1.2",
        gspp_title="Verpflichtung der Institutionsleitung",
        gs_ids=["ISMS.1.A1"],
        coverage="voll",
        confidence=0.95,
        rationale="ISMS.1.A1 beschreibt die Übernahme der Gesamtverantwortung durch die Institutionsleitung, deckt also die Kernanforderung vollständig ab.",
    ),
    GoldenMapping(
        gspp_id="GC.6.1.3",
        gspp_title="Erstellung einer Sicherheitsleitlinie",
        gs_ids=["ISMS.1.A3"],
        coverage="voll",
        confidence=0.95,
        rationale="ISMS.1.A3 'Erstellung einer Leitlinie zur Informationssicherheit' deckt die Anforderung identisch ab.",
    ),
    GoldenMapping(
        gspp_id="GC.6.1.4",
        gspp_title="Freigabe der Sicherheitsleitlinie",
        gs_ids=["ISMS.1.A3"],
        coverage="voll",
        confidence=0.95,
        rationale="ISMS.1.A3 enthält explizit die Freigabe und Verabschiedung durch die Institutionsleitung.",
    ),
    
    # Rollen und Verantwortlichkeiten
    GoldenMapping(
        gspp_id="GC.8.1.1.1",
        gspp_title="Informationssicherheitsbeauftragter",
        gs_ids=["ISMS.1.A4"],
        coverage="voll",
        confidence=0.95,
        rationale="ISMS.1.A4 beschreibt die Benennung eines ISB mit Berichtslinie zur Leitung - identisch zur GS++-Anforderung.",
    ),
    GoldenMapping(
        gspp_id="GC.8.1.2",
        gspp_title="Stellvertreterregelungen",
        gs_ids=["ISMS.1.A6"],
        coverage="voll",
        confidence=0.90,
        rationale="ISMS.1.A6 legt Vertretungsregelungen für wichtige Funktionen fest, deckt also die Anforderung ab.",
    ),
    
    # Kontext der Institution - Teilweise Abdeckungen
    GoldenMapping(
        gspp_id="GC.2.1",
        gspp_title="Festlegung des externen Kontextes der Institution",
        gs_ids=["ORP.5.A1", "ORP.5.A4"],
        coverage="teilweise",
        confidence=0.65,
        rationale="ORP.5.A1 und ORP.5.A4 decken gesetzliche/vertragliche Rahmenbedingungen ab. Fehlend: gesellschaftliche, technologische, ökonomische Faktoren außerhalb rechtlicher Vorgaben.",
        notes="Gap: Breitere externe Faktoren (PEST-Analyse) nicht im klassischen Grundschutz abgedeckt.",
    ),
    GoldenMapping(
        gspp_id="GC.2.2",
        gspp_title="Festlegung des internen Kontextes der Institution",
        gs_ids=["ISMS.1.A2"],
        coverage="teilweise",
        confidence=0.60,
        rationale="ISMS.1.A2 deckt organisatorische Rahmenbedingungen teilweise ab. Fehlend: Detaillierte interne Analyse (Strukturen, Kultur, interne Stakeholder).",
        notes="Gap: Interner Kontext ist im Grundschutz weniger detailliert spezifiziert.",
    ),
    
    # Risikomanagement
    GoldenMapping(
        gspp_id="GC.11.1",
        gspp_title="Methodik für das Risikomanagement",
        gs_ids=["ISMS.1.A9"],
        coverage="teilweise",
        confidence=0.60,
        rationale="ISMS.1.A9 behandelt Integration in Risikomanagement. Fehlend: Spezifische Methodik, verbindliche Dokumentation von Risikoeinstufung und -behandlung.",
        notes="Gap: Detaillierte Risikomanagement-Methodik ist in GS++ expliziter gefordert.",
    ),
    GoldenMapping(
        gspp_id="GC.5.1.2",
        gspp_title="Festlegung des Schutzbedarfs",
        gs_ids=["ISMS.1.A10"],
        coverage="teilweise",
        confidence=0.70,
        rationale="ISMS.1.A10 behandelt Schutzbedarfsanalyse im Rahmen des Sicherheitskonzepts. Fehlend: Spezifische Einstufung 'normal'/'hoch' und Methodik.",
    ),
    
    # Geltungsbereich
    GoldenMapping(
        gspp_id="GC.4.1",
        gspp_title="Festlegung des Geltungsbereichs",
        gs_ids=["ISMS.1.A3"],
        coverage="teilweise",
        confidence=0.70,
        rationale="ISMS.1.A3 behandelt den Geltungsbereich in der Sicherheitsleitlinie. Fehlend: Infrastrukturelle Abgrenzung und Einbeziehung externer Partner.",
    ),
    
    # ISMS-Einrichtung
    GoldenMapping(
        gspp_id="GC.1.1",
        gspp_title="Errichtung und Aufrechterhaltung eines ISMS",
        gs_ids=["ISMS.1.A1", "ISMS.1.A2", "ISMS.1.A3"],
        coverage="teilweise",
        confidence=0.75,
        rationale="Die ISMS-Bausteine decken Grundelemente ab. Fehlend: Explizite kontinuierliche Überprüfung und detaillierte ISMS-Regelungen.",
        notes="Diese Anforderung ist sehr breit und erfordert mehrere GS-Anforderungen für teilweise Abdeckung.",
    ),
    
    # Compliance
    GoldenMapping(
        gspp_id="GC.7.1.1",
        gspp_title="Gesetzliche Verpflichtungen",
        gs_ids=["ORP.5.A1", "ORP.5.A4"],
        coverage="teilweise",
        confidence=0.70,
        rationale="ORP.5 deckt gesetzliche Rahmenbedingungen ab. Fehlend: Spezifische Anforderungen zur Dokumentation und regelmäßigen Überprüfung.",
    ),
    
    # Beispiele für 'keine' Abdeckung (spezifische GS++-Anforderungen ohne GS-Äquivalent)
    GoldenMapping(
        gspp_id="GC.3.2",
        gspp_title="Analyse der Anforderungen interessierter Parteien",
        gs_ids=[],
        coverage="keine",
        confidence=0.20,
        rationale="Der klassische Grundschutz hat keinen expliziten Prozess zur systematischen Analyse von Stakeholder-Anforderungen über Compliance hinaus.",
        notes="Systematisches Stakeholder-Requirements-Management ist neu in GS++.",
    ),
]


def get_golden_mapping(gspp_id: str) -> GoldenMapping | None:
    """Get a golden mapping by GS++ ID."""
    for mapping in GOLDEN_MAPPINGS:
        if mapping.gspp_id == gspp_id:
            return mapping
    return None


def evaluate_match(match, golden: GoldenMapping) -> dict[str, float | bool | str]:
    """Evaluate a match against golden ground truth.
    
    Returns metrics:
    - coverage_correct: bool - coverage level matches
    - precision: float - of matched GS IDs, how many are correct
    - recall: float - of golden GS IDs, how many were found
    - f1: float - harmonic mean of precision and recall
    - confidence_error: float - absolute error in confidence score
    """
    
    # Coverage accuracy
    coverage_correct = match.coverage == golden.coverage
    
    # Calculate precision/recall for GS IDs
    match_ids = set(match.gs_candidates)
    golden_ids = set(golden.gs_ids)
    
    if match_ids and golden_ids:
        tp = len(match_ids & golden_ids)  # True positives
        fp = len(match_ids - golden_ids)  # False positives
        fn = len(golden_ids - match_ids)  # False negatives
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    elif not match_ids and not golden_ids:
        # Both empty - correct 'keine' mapping
        precision = recall = f1 = 1.0
    else:
        # One empty, one not - complete mismatch
        precision = recall = f1 = 0.0
    
    confidence_error = abs(match.confidence - golden.confidence)
    
    return {
        "coverage_correct": coverage_correct,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confidence_error": confidence_error,
        "gs_ids_tp": len(match_ids & golden_ids) if match_ids and golden_ids else 0,
        "gs_ids_fp": len(match_ids - golden_ids) if match_ids else 0,
        "gs_ids_fn": len(golden_ids - match_ids) if golden_ids else 0,
    }


def evaluate_matches(matches: list[Match]) -> dict[str, float | int]:
    """Evaluate a list of matches against golden mappings."""
    total_metrics = {
        "total_evaluated": 0,
        "coverage_correct": 0,
        "precision_sum": 0.0,
        "recall_sum": 0.0,
        "f1_sum": 0.0,
        "confidence_error_sum": 0.0,
        "total_tp": 0,
        "total_fp": 0,
        "total_fn": 0,
    }
    
    for match in matches:
        golden = get_golden_mapping(match.gspp_id)
        if golden is None:
            continue
        
        metrics = evaluate_match(match, golden)
        total_metrics["total_evaluated"] += 1
        total_metrics["coverage_correct"] += int(metrics["coverage_correct"])
        total_metrics["precision_sum"] += metrics["precision"]
        total_metrics["recall_sum"] += metrics["recall"]
        total_metrics["f1_sum"] += metrics["f1"]
        total_metrics["confidence_error_sum"] += metrics["confidence_error"]
        total_metrics["total_tp"] += metrics["gs_ids_tp"]
        total_metrics["total_fp"] += metrics["gs_ids_fp"]
        total_metrics["total_fn"] += metrics["gs_ids_fn"]
    
    n = total_metrics["total_evaluated"]
    if n == 0:
        return {"evaluated": 0}
    
    # Calculate micro and macro averages
    micro_precision = total_metrics["total_tp"] / (total_metrics["total_tp"] + total_metrics["total_fp"]) if (total_metrics["total_tp"] + total_metrics["total_fp"]) > 0 else 0.0
    micro_recall = total_metrics["total_tp"] / (total_metrics["total_tp"] + total_metrics["total_fn"]) if (total_metrics["total_tp"] + total_metrics["total_fn"]) > 0 else 0.0
    micro_f1 = 2 * micro_precision * micro_recall / (micro_precision + micro_recall) if (micro_precision + micro_recall) > 0 else 0.0
    
    return {
        "evaluated": n,
        "coverage_accuracy": total_metrics["coverage_correct"] / n,
        "macro_precision": total_metrics["precision_sum"] / n,
        "macro_recall": total_metrics["recall_sum"] / n,
        "macro_f1": total_metrics["f1_sum"] / n,
        "micro_precision": micro_precision,
        "micro_recall": micro_recall,
        "micro_f1": micro_f1,
        "avg_confidence_error": total_metrics["confidence_error_sum"] / n,
        "total_tp": total_metrics["total_tp"],
        "total_fp": total_metrics["total_fp"],
        "total_fn": total_metrics["total_fn"],
    }


def print_evaluation_report(metrics: dict[str, float | int]) -> None:
    """Print a formatted evaluation report."""
    print("\n" + "=" * 50)
    print("GOLDEN DATASET EVALUATION REPORT")
    print("=" * 50)
    
    if metrics.get("evaluated", 0) == 0:
        print("No matches evaluated against golden dataset.")
        return
    
    print(f"\nEvaluated: {metrics['evaluated']} mappings")
    print()
    print(f"Coverage Accuracy:     {metrics['coverage_accuracy']:.1%}")
    print()
    print("GS ID Matching (Macro):")
    print(f"  Precision:           {metrics['macro_precision']:.1%}")
    print(f"  Recall:              {metrics['macro_recall']:.1%}")
    print(f"  F1 Score:            {metrics['macro_f1']:.1%}")
    print()
    print("GS ID Matching (Micro):")
    print(f"  Precision:           {metrics['micro_precision']:.1%}")
    print(f"  Recall:              {metrics['micro_recall']:.1%}")
    print(f"  F1 Score:            {metrics['micro_f1']:.1%}")
    print()
    print(f"Avg Confidence Error:  {metrics['avg_confidence_error']:.2f}")
    print()
    print("Confusion Matrix:")
    print(f"  True Positives:      {metrics['total_tp']}")
    print(f"  False Positives:     {metrics['total_fp']}")
    print(f"  False Negatives:     {metrics['total_fn']}")
    print("=" * 50)
