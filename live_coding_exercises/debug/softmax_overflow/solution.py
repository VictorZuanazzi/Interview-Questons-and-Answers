"""Debug drill: overflowing vs stable softmax."""

import numpy as np


def softmax_broken(x):
    e = np.exp(x)
    return e / e.sum()


def softmax_fixed(x):
    x = np.asarray(x, dtype=float)
    z = x - x.max()
    e = np.exp(z)
    return e / e.sum()
