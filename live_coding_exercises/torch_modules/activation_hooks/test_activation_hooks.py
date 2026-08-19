from pathlib import Path

import torch
import torch.nn as nn
import pytest

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
collect_activations = impl.collect_activations


class Tiny(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 4)
        self.fc2 = nn.Linear(4, 2)

    def forward(self, x):
        return self.fc2(torch.relu(self.fc1(x)))


@pytest.fixture
def model():
    return Tiny()


@pytest.fixture
def activations(model):
    return collect_activations(model, torch.randn(3, 4), ["fc1", "fc2"])


def test_returns_only_requested_layers(activations):
    assert set(activations) == {"fc1", "fc2"}


def test_shapes_match_layer_outputs(activations):
    assert activations["fc1"].shape == (3, 4)
    assert activations["fc2"].shape == (3, 2)


def test_can_collect_a_single_layer(model):
    activations = collect_activations(model, torch.randn(1, 4), ["fc2"])
    assert list(activations) == ["fc2"]


def test_tensors_are_detached(activations):
    assert not any(tensor.requires_grad for tensor in activations.values())


def test_hooks_are_removed_afterwards(model, activations):
    assert len(model.fc1._forward_hooks) == 0
    assert len(model.fc2._forward_hooks) == 0
