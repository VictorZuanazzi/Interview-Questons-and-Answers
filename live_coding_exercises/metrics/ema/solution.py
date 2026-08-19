"""Exponential moving average over a stream of values."""


def exponential_moving_average(values, momentum=0.9):
    """Return EMA state after each update: ema = momentum * ema + (1 - momentum) * x"""
    out, ema = [], None
    for x in values:
        ema = x if ema is None else momentum * ema + (1 - momentum) * x
        out.append(ema)
    return out
