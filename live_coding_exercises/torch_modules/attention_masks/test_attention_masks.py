from pathlib import Path

import numpy as np
import pytest
import torch
import torch.nn as nn

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
causal_mask = impl.causal_mask
key_padding_mask = impl.key_padding_mask


def _torch_causal_bool(seq_len):
    # generate_square_subsequent_mask: float with -inf above diagonal; convert to bool blocked
    mask = nn.Transformer.generate_square_subsequent_mask(seq_len)
    return mask.eq(float("-inf")).numpy()


def _torch_key_padding(lengths, max_len):
    lengths_t = torch.as_tensor(lengths)
    return (torch.arange(max_len)[None, :] >= lengths_t[:, None]).numpy()


@pytest.fixture
def mask():
    return np.asarray(causal_mask(3))


def test_causal_mask_matches_torch_and_triu(mask):
    assert mask.dtype == bool
    assert np.array_equal(mask, np.triu(np.ones((3, 3), dtype=bool), k=1))
    assert np.array_equal(mask, _torch_causal_bool(3))


def test_causal_mask_allows_self_and_past(mask):
    assert not mask[0, 0]
    assert not mask[2, 0]


def test_causal_mask_blocks_future(mask):
    assert mask[0, 2]
    assert mask[1, 2]


@pytest.mark.parametrize(
    "lengths, max_len",
    [
        ([2, 3], 3),
        ([1, 2, 4], 4),
        ([0, 3], 3),
    ],
)
def test_key_padding_mask_matches_torch(lengths, max_len):
    got = np.asarray(key_padding_mask(lengths, max_len))
    expected = _torch_key_padding(lengths, max_len)
    assert np.array_equal(got, expected)


def test_key_padding_mask_counts_match_lengths():
    lengths = [1, 2, 4]
    padding = np.asarray(key_padding_mask(lengths, max_len=4))
    assert (~padding).sum(axis=-1).tolist() == lengths
