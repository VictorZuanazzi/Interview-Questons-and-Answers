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
    
    return (np.round(x / scale) + zero_point).clip(min=qmin, max=qmax).astype(np.int8)


def dequantize_affine(q: np.ndarray, scale: float, zero_point: int) -> np.ndarray:
    """x_hat = scale * (q - zero_point)"""
    
    return scale * (q - zero_point)

def sqnr_db(x: np.ndarray, x_hat: np.ndarray, eps: float = 1e-12) -> float:
    """10 * log10(mean(x^2) / (mean((x - x_hat)^2) + eps))"""

    signal = (x ** 2).mean()
    noise = ((x - x_hat) ** 2).mean()
    sqnr = np.log10(signal) - np.log10(noise + eps)
    return 10 * sqnr


x = (np.arange(5) - np.pi / 2) ** 3 
scale = abs(x).max() / 127
print(x)
q = quantize_affine(x, scale, 0)
print(q)
x_hat = dequantize_affine(q, scale, 0)
print(x_hat)
print(sqnr_db(x, x_hat))