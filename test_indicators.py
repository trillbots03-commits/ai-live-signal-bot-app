from app.indicators.engine import ema, rsi, atr


def test_ema_insufficient_history():
    assert ema([1, 2], 9) is None


def test_rsi_flat_market():
    assert rsi([1.0] * 20) == 50.0


def test_atr_rejects_mismatched_lengths():
    try:
        atr([1], [1, 2], [1])
    except ValueError:
        return
    raise AssertionError("expected ValueError")
