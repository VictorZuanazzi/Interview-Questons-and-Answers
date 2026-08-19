"""Debug drill: attention score matmul and scaling."""

import math

import torch


def attention_scores_broken(Q, K):
    # BUGS: wrong transpose; missing 1/sqrt(d); mask broadcast
    return Q @ K


def attention_scores_fixed(Q, K, mask=None):
    """Q,K: (B, H, T, D). Return scores (B, H, T, T), scaled.
    Optional mask: True means masked (set to -inf).
    """
    raise NotImplementedError
