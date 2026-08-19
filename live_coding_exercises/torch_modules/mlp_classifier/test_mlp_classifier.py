from pathlib import Path

import torch
import torch.nn as nn

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
MLPClassifier = impl.MLPClassifier


def test_output_shape():
    model = MLPClassifier(4, 8, 3)
    assert model(torch.randn(2, 4)).shape == (2, 3)


def test_has_two_linear_layers():
    model = MLPClassifier(4, 8, 3)
    linears = [m for m in model.modules() if isinstance(m, nn.Linear)]
    assert len(linears) == 2
    assert linears[0].in_features == 4
    assert linears[-1].out_features == 3


def test_returns_logits_not_probabilities():
    model = MLPClassifier(4, 8, 3)
    assert not any(isinstance(m, nn.Softmax) for m in model.modules())


def test_forward_is_differentiable():
    model = MLPClassifier(4, 8, 3)
    loss = model(torch.randn(2, 4)).sum()
    loss.backward()
    assert all(p.grad is not None for p in model.parameters())


def test_handles_single_sample_batch():
    model = MLPClassifier(4, 8, 3)
    assert model(torch.randn(1, 4)).shape == (1, 3)
