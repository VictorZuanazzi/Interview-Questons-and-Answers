"""One-hot encoding and row gather."""

import numpy as np


def one_hot(indices, n_classes):
    """indices (N,) -> (N, C) float array."""
    raise NotImplementedError


def gather_rows(mat, indices):
    """mat (N, C), indices (N,) -> (N,) values mat[i, indices[i]]."""
    raise NotImplementedError
