from datetime import datetime, timezone


SUPPORTED = {"EUR/USD", "BTC/USD", "NAS100"}


def analyze_market(symbol: str) -> dict:
    normalized = symbol.upper()
    if normalized not in SUPPORTED:
        return {"symbol": normalized, "decision": "WAIT", "state": "BLOCKED",
                "reason": "Unsupported market"}
    return {
        "symbol": normalized,
        "decision": "WAIT",
        "state": "BLOCKED",
        "data_quality": "BLOCKED",
        "reason": "Verified live market data is not configured",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "a_plus": {"eligible": False, "score": 0},
    }
