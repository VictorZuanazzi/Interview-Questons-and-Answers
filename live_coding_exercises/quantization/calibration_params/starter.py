"""Derive affine quantize scale and zero-point from a value range."""

import numpy as np


def calibration_params(
    x_min: float,
    x_max: float,
    qmin: int = 0,
    qmax: int = 255,
) -> tuple[float, int]:
    """Return (scale, zero_point) for affine quantization."""
    raise NotImplementedError
