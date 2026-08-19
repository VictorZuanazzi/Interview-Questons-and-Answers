"""Stable softmax, temperature softmax, and log-softmax."""

import numpy as np


def softmax(logits: np.ndarray) -> np.ndarray:
    """logits: 1D or 2D numpy array (batch, classes) if 2D.

    Return probabilities with the same shape. Numerically stable.
    """
    raise NotImplementedError


def softmax_temperature(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    """Stable softmax with temperature > 0.

    T=1 -> standard softmax; T>1 softer; 0<T<1 sharper.
    """
    raise NotImplementedError


def log_softmax(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    """Stable log(softmax(logits / T)). Avoid log(softmax(...)) for numerics."""
    raise NotImplementedError
