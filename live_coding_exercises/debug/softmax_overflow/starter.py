"""Debug drill: overflowing vs stable softmax."""

import numpy as np


def softmax_broken(x: np.ndarray) -> np.ndarray:
    e = np.exp(x)
    return e / e.sum()


def softmax_fixed(x: np.ndarray) -> np.ndarray:
    # YOUR FIX HERE
    raise NotImplementedError
