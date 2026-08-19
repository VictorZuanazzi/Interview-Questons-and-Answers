"""Derive affine quantize scale and zero-point from a value range."""

import numpy as np


def calibration_params(x_min, x_max, qmin=0, qmax=255):
    """Return (scale, zero_point) for affine quantization."""
    raise NotImplementedError
