"""Vectorized pairwise Euclidean distances."""

import numpy as np


def pairwise_l2(a, b):
    """Return (N, M) pairwise Euclidean distances."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    aa = (a * a).sum(axis=1, keepdims=True)
    bb = (b * b).sum(axis=1, keepdims=True).T
    d2 = np.maximum(aa + bb - 2 * a @ b.T, 0.0)
    return np.sqrt(d2)
