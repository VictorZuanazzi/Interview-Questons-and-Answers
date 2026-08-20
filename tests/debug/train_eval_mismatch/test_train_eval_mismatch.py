import pytest
import torch

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
DropNet = impl.DropNet
predict_broken = impl.predict_broken
predict_fixed = impl.predict_fixed


@pytest.fixture
def model():
    torch.manual_seed(0)
    return DropNet()


@pytest.fixture
def batch():
    torch.manual_seed(1)
    return torch.randn(32, 4)


def test_broken_version_is_nondeterministic(model, batch):
    with torch.no_grad():
        first, second = predict_broken(model, batch), predict_broken(model, batch)
    assert not torch.allclose(first, second)


def test_fixed_version_is_deterministic(model, batch):
    with torch.no_grad():
        first, second = predict_fixed(model, batch), predict_fixed(model, batch)
    assert torch.allclose(first, second)


def test_fixed_version_switches_module_to_eval(model, batch):
    with torch.no_grad():
        predict_fixed(model, batch)
    assert not model.training


def test_fixed_version_disables_dropout_scaling(model, batch):
    with torch.no_grad():
        assert torch.allclose(predict_fixed(model, batch), model.fc(batch))


def test_output_shape_is_unchanged(model, batch):
    with torch.no_grad():
        assert predict_fixed(model, batch).shape == (32, 2)
