"""Causal and key-padding attention masks."""

import numpy as np


def causal_mask(seq_len: int) -> np.ndarray:
    """Boolean mask where position i cannot attend to j > i.
    Shape (seq_len, seq_len). True means MASKED (blocked).
    """
    
    mask_ones = np.ones((seq_len, seq_len), dtype=bool)   
    mask = np.triu(mask_ones, k=1)

    return mask

def _causal_mask(seq_len: int) -> np.ndarray:
    """Boolean mask where position i cannot attend to j > i.
    Shape (seq_len, seq_len). True means MASKED (blocked).

    Answer if np.triu isn't known.
    """
    mask = np.ones((seq_len, seq_len), dtype=bool)

    for i in range(seq_len):
        cols = (np.ones(i + 1,) * i).astype(int)
        rows = np.arange(i + 1, dtype=int)
        mask[cols, rows] = False

    return mask
    
def __causal_mask(seq_len: int) -> np.ndarray:
    att_len = np.arange(seq_len)
    mask = att_len[None, :] > att_len[:, None]

    return mask


def key_padding_mask(lengths: np.ndarray | list[int], max_len: int) -> np.ndarray:
    """True for pad positions. lengths: list/array of ints. Shape (B, max_len)."""
    
    lengths = np.array(lengths)
    mask = np.arange(max_len)[None, :] >= lengths[:, None]

    return mask


