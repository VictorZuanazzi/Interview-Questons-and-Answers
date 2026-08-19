"""Exponential moving average over a stream of values."""

from collections.abc import Sequence


def exponential_moving_average(
    values: Sequence[float],
    momentum: float = 0.9,
) -> list[float]:
    """Return EMA state after each update: ema = momentum * ema + (1 - momentum) * x"""
    out, ema = [], None
    for x in values:
        ema = x if ema is None else momentum * ema + (1 - momentum) * x
        out.append(ema)
    return out
