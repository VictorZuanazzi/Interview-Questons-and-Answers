"""Affine quantization helpers."""

import numpy as np


def quantize_affine(x, scale, zero_point, qmin=-128, qmax=127):
    """q = clip(round(x / scale) + zero_point, qmin, qmax)"""
    q = np.round(np.asarray(x, dtype=float) / scale) + zero_point
    return np.clip(q, qmin, qmax).astype(np.int32)


def dequantize_affine(q, scale, zero_point):
    """x_hat = scale * (q - zero_point)"""
    return scale * (np.asarray(q, dtype=float) - zero_point)


def sqnr_db(x, x_hat, eps=1e-12):
    signal = np.mean(np.asarray(x, dtype=float) ** 2)
    noise = np.mean((np.asarray(x, dtype=float) - np.asarray(x_hat, dtype=float)) ** 2)
    return 10 * np.log10(signal / (noise + eps))
