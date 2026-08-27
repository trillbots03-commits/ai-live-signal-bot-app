from hypothesis import given, strategies as st
from app.indicators.engine import ema, rsi


finite_lists = st.lists(
    st.floats(min_value=0.000001, max_value=1_000_000, allow_nan=False, allow_infinity=False),
    min_size=1,
    max_size=200,
)


@given(finite_lists)
def test_ema_is_none_or_finite(values):
    result = ema(values, min(9, len(values) + 1))
    assert result is None or result == result


@given(finite_lists)
def test_rsi_is_bounded(values):
    result = rsi(values)
    assert result is None or 0 <= result <= 100
