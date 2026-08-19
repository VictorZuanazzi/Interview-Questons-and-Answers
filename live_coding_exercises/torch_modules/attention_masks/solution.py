"""Causal and key-padding attention masks."""

import numpy as np


def causal_mask(seq_len):
    """Boolean mask where position i cannot attend to j > i.
    Shape (seq_len, seq_len). True means MASKED (blocked).
    """
    return np.triu(np.ones((seq_len, seq_len), dtype=bool), k=1)


def key_padding_mask(lengths, max_len):
    """True for pad positions. lengths: list/array of ints. Shape (B, max_len)."""
    lengths = np.asarray(lengths)
    return np.arange(max_len)[None, :] >= lengths[:, None]
