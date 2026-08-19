"""Debug drill: attention score matmul and scaling."""

import math

import torch


def attention_scores_broken(Q: torch.Tensor, K: torch.Tensor) -> torch.Tensor:
    # BUGS: wrong transpose; missing 1/sqrt(d); mask broadcast
    return Q @ K


def attention_scores_fixed(
    Q: torch.Tensor,
    K: torch.Tensor,
    mask: torch.Tensor | None = None,
) -> torch.Tensor:
    """Q,K: (B, H, T, D). Return scores (B, H, T, T), scaled.
    Optional mask: True means masked (set to -inf).
    """
    D = Q.shape[-1]
    scores = Q @ K.transpose(-2, -1) / math.sqrt(D)
    if mask is not None:
        scores = scores.masked_fill(mask, float("-inf"))
    return scores
