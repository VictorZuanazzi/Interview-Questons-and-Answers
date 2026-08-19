"""Causal and key-padding attention masks."""

import numpy as np


def causal_mask(seq_len: int) -> np.ndarray:
    """Boolean mask where position i cannot attend to j > i.
    Shape (seq_len, seq_len). True means MASKED (blocked).
    """
    raise NotImplementedError


def key_padding_mask(lengths: np.ndarray | list[int], max_len: int) -> np.ndarray:
    """True for pad positions. lengths: list/array of ints. Shape (B, max_len)."""
    raise NotImplementedError
