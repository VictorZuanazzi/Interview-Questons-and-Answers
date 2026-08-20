import pytest
import torch

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
sgd_step = impl.sgd_step


def _torch_sgd_step(params, grads, lr, weight_decay=0.0):
    clones = [p.detach().clone().requires_grad_(True) for p in params]
    for p, g in zip(clones, grads):
        p.grad = g.detach().clone()
    opt = torch.optim.SGD(clones, lr=lr, weight_decay=weight_decay)
    opt.step()
    return [p.detach() for p in clones]


def test_matches_torch_optim_sgd_basic():
    params = [torch.tensor([1.0, 2.0])]
    grads = [torch.tensor([0.5, -0.5])]
    got = sgd_step(params, grads, lr=0.1)
    expected = _torch_sgd_step(params, grads, lr=0.1)
    assert torch.allclose(got[0], expected[0])


def test_zero_learning_rate_is_a_noop():
    param = torch.tensor([1.0, -3.0])
    updated = sgd_step([param], [torch.tensor([9.0, 9.0])], lr=0.0)
    assert torch.allclose(updated[0], param)


def test_weight_decay_matches_torch_optim():
    param = torch.tensor([2.0])
    grad = torch.tensor([1.0])
    got = sgd_step([param], [grad], lr=0.1, weight_decay=0.5)[0]
    expected = _torch_sgd_step([param], [grad], lr=0.1, weight_decay=0.5)[0]
    assert torch.allclose(got, expected)


def test_weight_decay_pulls_parameters_towards_zero():
    param = torch.tensor([2.0])
    no_decay = sgd_step([param], [torch.zeros(1)], lr=0.1, weight_decay=0.0)[0]
    with_decay = sgd_step([param], [torch.zeros(1)], lr=0.1, weight_decay=0.5)[0]
    assert with_decay.item() < no_decay.item() == pytest.approx(2.0)


def test_updates_every_parameter():
    params = [torch.tensor([1.0]), torch.tensor([[1.0, 1.0]])]
    grads = [torch.tensor([1.0]), torch.ones(1, 2)]
    updated = sgd_step(params, grads, lr=0.5)
    expected = _torch_sgd_step(params, grads, lr=0.5)
    assert len(updated) == 2
    assert torch.allclose(updated[0], expected[0])
    assert torch.allclose(updated[1], expected[1])
