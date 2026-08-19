"""Stable softmax, temperature softmax, and log-softmax."""

import numpy as np


def softmax(logits):
    """logits: 1D or 2D numpy array (batch, classes) if 2D.

    Return probabilities with the same shape. Numerically stable.
    """
    logits = np.asarray(logits, dtype=float)
    shifted = logits - logits.max(axis=-1, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=-1, keepdims=True)


def softmax_temperature(logits, temperature=1.0):
    """Stable softmax with temperature > 0.

    T=1 -> standard softmax; T>1 softer; 0<T<1 sharper.
    """
    logits = np.asarray(logits, dtype=float)
    temp_logits = logits / temperature
    shifted = temp_logits - temp_logits.max(axis=-1, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=-1, keepdims=True)


def log_softmax(logits, temperature=1.0):
    """Stable log(softmax(logits / T)). Avoid log(softmax(...)) for numerics."""
    logits = np.asarray(logits, dtype=float)
    temp_logits = logits / temperature
    shifted = temp_logits - temp_logits.max(axis=-1, keepdims=True)
    return shifted - np.log(np.exp(shifted).sum(axis=-1, keepdims=True))
