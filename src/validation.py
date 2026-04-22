"""Validation utilities for GS++ → GS mapping quality assurance."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from .models import Match, Requirement


@dataclass
class ValidationIssue:
    """A validation issue found in a match."""
    severity: Literal["error", "warning", "info"]
    code: str
    message: str


class MatchValidator:
    """Validates matches for consistency and quality."""
    
    # Valid GS ID pattern: BAUSTEIN.NUMBER[.NUMBER...].ANUMBER
    # Examples: ISMS.1.A2, ORP.5.A10, SYS.3.2.1.A28, OPS.1.1.2.A16
    GS_ID_PATTERN = re.compile(r'^[A-Z]+(?:\.\d+)+\.A\d+$')
    
    # Coverage score mapping
    COVERAGE_SCORE = {"keine": 0, "teilweise": 1, "voll": 2}
    
    def __init__(self, gs_index: dict[str, Requirement] | None = None):
        self.gs_index = gs_index or {}
    
    def validate(self, match: Match, gspp_req: Requirement | None = None) -> list[ValidationIssue]:
        """Validate a match and return list of issues."""
        issues = []
        
        # 1. Validate GS IDs exist and have correct format
        for gid in match.gs_candidates:
            if not self.GS_ID_PATTERN.match(gid):
                issues.append(ValidationIssue(
                    severity="error",
                    code="INVALID_ID_FORMAT",
                    message=f"GS ID '{gid}' does not match expected format BAUSTEIN.NUMBER.ANUMBER"
                ))
            elif self.gs_index and gid not in self.gs_index:
                issues.append(ValidationIssue(
                    severity="error",
                    code="UNKNOWN_GS_ID",
                    message=f"GS ID '{gid}' not found in corpus"
                ))
        
        # 2. Validate coverage consistency
        if match.coverage not in self.COVERAGE_SCORE:
            issues.append(ValidationIssue(
                severity="error",
                code="INVALID_COVERAGE",
                message=f"Coverage '{match.coverage}' is not one of: voll, teilweise, keine"
            ))
        
        # 3. Check coverage/candidate consistency
        if match.coverage == "keine" and match.gs_candidates:
            issues.append(ValidationIssue(
                severity="warning",
                code="COVERAGE_MISMATCH",
                message=f"Coverage is 'keine' but {len(match.gs_candidates)} candidates listed"
            ))
        
        if match.coverage == "voll" and not match.gs_candidates:
            issues.append(ValidationIssue(
                severity="error",
                code="COVERAGE_MISMATCH",
                message="Coverage is 'voll' but no candidates provided"
            ))
        
        # 4. Validate confidence range
        if not 0.0 <= match.confidence <= 1.0:
            issues.append(ValidationIssue(
                severity="error",
                code="INVALID_CONFIDENCE",
                message=f"Confidence {match.confidence} is outside valid range [0.0, 1.0]"
            ))
        
        # 5. Check for confidence inflation (high confidence with partial coverage)
        if match.coverage == "teilweise" and match.confidence > 0.9:
            issues.append(ValidationIssue(
                severity="warning",
                code="CONFIDENCE_INFLATION",
                message=f"High confidence ({match.confidence:.2f}) with 'teilweise' coverage - possible overconfidence"
            ))
        
        # 6. Validate rationale mentions all candidates
        if match.rationale and match.gs_candidates:
            missing = [gid for gid in match.gs_candidates if gid not in match.rationale]
            if missing:
                issues.append(ValidationIssue(
                    severity="warning",
                    code="RATIONALE_INCOMPLETE",
                    message=f"Rationale does not mention candidates: {missing}"
                ))
        
        # 7. Check for empty rationale when candidates exist
        if match.gs_candidates and not match.rationale:
            issues.append(ValidationIssue(
                severity="warning",
                code="MISSING_RATIONALE",
                message="Candidates provided but no rationale given"
            ))
        
        # 8. Check gap_notes consistency
        if match.coverage == "voll" and match.gap_notes:
            issues.append(ValidationIssue(
                severity="info",
                code="UNNECESSARY_GAP_NOTES",
                message="Gap notes provided but coverage is 'voll'"
            ))
        
        if match.coverage == "teilweise" and not match.gap_notes:
            issues.append(ValidationIssue(
                severity="warning",
                code="MISSING_GAP_NOTES",
                message="Coverage is 'teilweise' but no gap notes provided"
            ))
        
        # 9. Check for excessive candidates (possible over-mapping)
        if len(match.gs_candidates) > 5:
            issues.append(ValidationIssue(
                severity="info",
                code="MANY_CANDIDATES",
                message=f"High number of candidates ({len(match.gs_candidates)}) - consider discrimination"
            ))
        
        # 10. Check GS++ ID matches match object
        if gspp_req and match.gspp_id != gspp_req.id:
            issues.append(ValidationIssue(
                severity="error",
                code="ID_MISMATCH",
                message=f"Match gspp_id '{match.gspp_id}' != requirement id '{gspp_req.id}'"
            ))
        
        return issues
    
    def is_valid(self, match: Match, gspp_req: Requirement | None = None, max_severity: Literal["error", "warning"] = "error") -> bool:
        """Check if match is valid up to given severity level."""
        issues = self.validate(match, gspp_req)
        severity_order = {"info": 0, "warning": 1, "error": 2}
        max_level = severity_order.get(max_severity, 2)
        return all(severity_order.get(i.severity, 0) < max_level for i in issues)


def validate_matches(
    matches: list[Match],
    gspp_index: dict[str, Requirement],
    gs_index: dict[str, Requirement],
) -> dict[str, list[ValidationIssue]]:
    """Validate all matches and return issues by gspp_id."""
    validator = MatchValidator(gs_index)
    return {
        match.gspp_id: validator.validate(match, gspp_index.get(match.gspp_id))
        for match in matches
    }


def print_validation_report(issues_by_id: dict[str, list[ValidationIssue]]) -> None:
    """Print a human-readable validation report."""
    total_issues = sum(len(issues) for issues in issues_by_id.values())
    errors = sum(1 for issues in issues_by_id.values() for i in issues if i.severity == "error")
    warnings = sum(1 for issues in issues_by_id.values() for i in issues if i.severity == "warning")
    
    print(f"\n=== Validation Report ===")
    print(f"Total issues: {total_issues} ({errors} errors, {warnings} warnings)")
    print()
    
    for gspp_id, issues in sorted(issues_by_id.items()):
        if not issues:
            continue
        print(f"{gspp_id}:")
        for issue in issues:
            icon = "🔴" if issue.severity == "error" else "🟡" if issue.severity == "warning" else "🔵"
            print(f"  {icon} [{issue.code}] {issue.message}")
        print()
