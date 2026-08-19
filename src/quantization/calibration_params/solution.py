"""Derive affine quantize scale and zero-point from a value range."""

import numpy as np


def calibration_params(
    x_min: float,
    x_max: float,
    qmin: int = 0,
    qmax: int = 255,
) -> tuple[float, int]:
    """Return (scale, zero_point) for affine quantization."""
    if x_max == x_min:
        x_max = x_min + 1e-8
    scale = (x_max - x_min) / (qmax - qmin)
    zp = int(np.clip(np.round(qmin - x_min / scale), qmin, qmax))
    return float(scale), zp
