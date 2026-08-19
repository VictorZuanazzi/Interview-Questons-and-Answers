"""Affine quantization helpers."""

import numpy as np


def quantize_affine(
    x: np.ndarray,
    scale: float,
    zero_point: int,
    qmin: int = -128,
    qmax: int = 127,
) -> np.ndarray:
    """q = clip(round(x / scale) + zero_point, qmin, qmax)"""
    raise NotImplementedError


def dequantize_affine(q: np.ndarray, scale: float, zero_point: int) -> np.ndarray:
    """x_hat = scale * (q - zero_point)"""
    raise NotImplementedError

def sqnr_db(x: np.ndarray, x_hat: np.ndarray, eps: float = 1e-12) -> float:
    """10 * log10(mean(x^2) / (mean((x - x_hat)^2) + eps))"""
    raise NotImplementedError