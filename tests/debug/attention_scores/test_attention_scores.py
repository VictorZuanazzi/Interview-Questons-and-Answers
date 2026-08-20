import math

import pytest
import torch

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
attention_scores_broken = impl.attention_scores_broken
attention_scores_fixed = impl.attention_scores_fixed

B, H, T, D = 2, 3, 4, 8


@pytest.fixture
def qk():
    torch.manual_seed(0)
    return torch.randn(B, H, T, D), torch.randn(B, H, T, D)


def test_broken_version_has_shape_mismatch(qk):
    Q, K = qk
    with pytest.raises(RuntimeError):
        attention_scores_broken(Q, K)


def test_scores_shape(qk):
    Q, K = qk
    assert attention_scores_fixed(Q, K).shape == (B, H, T, T)


def test_scores_match_scaled_matmul(qk):
    Q, K = qk
    expected = Q @ K.transpose(-2, -1) / math.sqrt(D)
    assert torch.allclose(attention_scores_fixed(Q, K), expected, atol=1e-5)


def test_mask_blocks_future_positions(qk):
    Q, K = qk
    mask = torch.triu(torch.ones(T, T, dtype=torch.bool), diagonal=1)
    scores = attention_scores_fixed(Q, K, mask=mask)
    assert torch.isneginf(scores[..., 0, -1]).all()
    assert torch.isfinite(scores[..., -1, 0]).all()


def test_masked_softmax_gives_zero_attention_to_future(qk):
    Q, K = qk
    mask = torch.triu(torch.ones(T, T, dtype=torch.bool), diagonal=1)
    weights = torch.softmax(attention_scores_fixed(Q, K, mask=mask), dim=-1)
    assert weights[..., 0, 1:] == pytest.approx(torch.zeros(B, H, T - 1).numpy(), abs=1e-6)
    assert weights.sum(-1) == pytest.approx(torch.ones(B, H, T).numpy(), abs=1e-5)
