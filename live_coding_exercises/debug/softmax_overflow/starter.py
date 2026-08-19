"""Debug drill: overflowing vs stable softmax."""

import numpy as np


def softmax_broken(x):
    e = np.exp(x)
    return e / e.sum()


def softmax_fixed(x):
    # YOUR FIX HERE
    raise NotImplementedError
