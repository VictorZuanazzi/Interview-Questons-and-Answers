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
    q = np.round(np.asarray(x, dtype=float) / scale) + zero_point
    return np.clip(q, qmin, qmax).astype(np.int32)


def dequantize_affine(q: np.ndarray, scale: float, zero_point: int) -> np.ndarray:
    """x_hat = scale * (q - zero_point)"""
    return scale * (np.asarray(q, dtype=float) - zero_point)


def sqnr_db(x: np.ndarray, x_hat: np.ndarray, eps: float = 1e-12) -> float:
    signal = np.mean(np.asarray(x, dtype=float) ** 2)
    noise = np.mean((np.asarray(x, dtype=float) - np.asarray(x_hat, dtype=float)) ** 2)
    return 10 * np.log10(signal / (noise + eps))
