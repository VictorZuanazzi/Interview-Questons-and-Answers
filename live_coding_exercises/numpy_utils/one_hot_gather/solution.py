"""One-hot encoding and row gather."""

import numpy as np


def one_hot(indices, n_classes):
    """indices (N,) -> (N, C) float array."""
    idx = np.asarray(indices)
    out = np.zeros((len(idx), n_classes), dtype=float)
    out[np.arange(len(idx)), idx] = 1.0
    return out


def gather_rows(mat, indices):
    """mat (N, C), indices (N,) -> (N,) values mat[i, indices[i]]."""
    mat = np.asarray(mat)
    indices = np.asarray(indices)
    return mat[np.arange(len(indices)), indices]
