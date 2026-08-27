from __future__ import annotations

from dataclasses import dataclass
from math import isnan
from typing import Sequence


@dataclass(frozen=True)
class IndicatorSet:
    ema9: float | None
    ema21: float | None
    ema50: float | None
    rsi14: float | None
    atr14: float | None


def _ema(values: Sequence[float], period: int) -> float | None:
    if len(values) < period:
        return None
    alpha = 2 / (period + 1)
    value = sum(values[:period]) / period
    for price in values[period:]:
        value = alpha * price + (1 - alpha) * value
    return value


def ema(values: Sequence[float], period: int) -> float | None:
    if period <= 0 or any(not isinstance(x, (int, float)) or not isfinite(x) for x in values):
        raise ValueError("values must contain finite numbers and period must be positive")
    return _ema(values, period)


def isfinite(value: float) -> bool:
    return value == value and abs(value) != float("inf")


def rsi(values: Sequence[float], period: int = 14) -> float | None:
    if period <= 0:
        raise ValueError("period must be positive")
    if len(values) < period + 1:
        return None
    gains = []
    losses = []
    for a, b in zip(values[:-1], values[1:]):
        delta = b - a
        gains.append(max(delta, 0))
        losses.append(max(-delta, 0))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for gain, loss in zip(gains[period:], losses[period:]):
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period
    if avg_loss == 0:
        return 100.0 if avg_gain else 50.0
    return 100 - (100 / (1 + avg_gain / avg_loss))


def atr(highs: Sequence[float], lows: Sequence[float], closes: Sequence[float],
        period: int = 14) -> float | None:
    if len(highs) != len(lows) or len(lows) != len(closes):
        raise ValueError("OHLC arrays must have equal lengths")
    if len(closes) < period + 1:
        return None
    true_ranges = []
    for i in range(1, len(closes)):
        true_ranges.append(max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1]),
        ))
    if len(true_ranges) < period:
        return None
    return sum(true_ranges[:period]) / period


def calculate(closes: Sequence[float], highs: Sequence[float] | None = None,
              lows: Sequence[float] | None = None) -> IndicatorSet:
    highs = highs or closes
    lows = lows or closes
    return IndicatorSet(
        ema9=ema(closes, 9),
        ema21=ema(closes, 21),
        ema50=ema(closes, 50),
        rsi14=rsi(closes),
        atr14=atr(highs, lows, closes),
    )
