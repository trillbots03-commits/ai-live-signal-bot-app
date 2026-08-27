from dataclasses import dataclass


@dataclass(frozen=True)
class GateResult:
    eligible: bool
    reason: str


def a_plus_gate(score: int, hard_requirements: dict[str, bool], ai_valid: bool,
                 fresh: bool, min_score: int = 92) -> GateResult:
    if score < min_score:
        return GateResult(False, "score below A+ threshold")
    if not all(hard_requirements.values()):
        return GateResult(False, "critical hard gate failed")
    if not ai_valid:
        return GateResult(False, "AI response invalid or unavailable")
    if not fresh:
        return GateResult(False, "signal is stale")
    return GateResult(True, "A+ approved")
