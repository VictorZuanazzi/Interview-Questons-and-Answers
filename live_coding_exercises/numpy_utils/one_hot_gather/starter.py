"""One-hot encoding and row gather."""

import numpy as np


def one_hot(indices: np.ndarray, n_classes: int) -> np.ndarray:
    """indices (N,) -> (N, C) float array."""
    raise NotImplementedError


def gather_rows(mat: np.ndarray, indices: np.ndarray) -> np.ndarray:
    """mat (N, C), indices (N,) -> (N,) values mat[i, indices[i]]."""
    raise NotImplementedError
