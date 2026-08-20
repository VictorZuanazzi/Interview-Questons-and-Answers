import numpy as np
import pytest
import torch
import torch.nn.functional as F
from scipy.special import softmax as scipy_softmax

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
softmax = impl.softmax
softmax_temperature = impl.softmax_temperature
log_softmax = impl.log_softmax

HUGE = np.array([1e5, 1e5 + 1.0, 1e5 + 2.0])
TINY = np.array([-1e5, -1e5 - 1.0, -1e5 - 2.0])


def _torch_softmax(logits, temperature=1.0):
    return F.softmax(torch.as_tensor(logits, dtype=torch.float64) / temperature, dim=-1).numpy()


def _torch_log_softmax(logits, temperature=1.0):
    return F.log_softmax(
        torch.as_tensor(logits, dtype=torch.float64) / temperature, dim=-1
    ).numpy()


@pytest.fixture
def logits_1d():
    return np.array([1.0, 2.0, 3.0])


@pytest.fixture
def logits_2d():
    return np.array([[1000.0, 1000.0], [1.0, 2.0]])


@pytest.fixture
def logits():
    return np.array([1.0, 2.0, 3.0])


@pytest.mark.parametrize(
    "logits",
    [
        np.array([1.0, 2.0, 3.0]),
        np.array([[1000.0, 1000.0], [1.0, 2.0]]),
        np.zeros(4),
        HUGE,
        TINY,
    ],
)
def test_softmax_matches_scipy_and_torch(logits):
    expected_scipy = scipy_softmax(logits, axis=-1)
    expected_torch = _torch_softmax(logits)
    got = softmax(logits)
    assert got == pytest.approx(expected_scipy)
    assert got == pytest.approx(expected_torch)


def test_softmax_is_shift_invariant_vs_scipy(logits_1d):
    shifted = logits_1d + 100.0
    assert softmax(shifted) == pytest.approx(scipy_softmax(shifted, axis=-1))
    assert softmax(logits_1d) == pytest.approx(softmax(shifted))


def test_naive_exp_overflows_but_scipy_and_impl_do_not():
    with np.errstate(over="ignore"):
        assert not np.isfinite(np.exp(HUGE)).all()
    assert np.isfinite(scipy_softmax(HUGE, axis=-1)).all()
    assert np.isfinite(softmax(HUGE)).all()


@pytest.mark.parametrize("temperature", [0.25, 1.0, 2.0, 10.0])
def test_temperature_matches_torch_and_scipy(logits, temperature):
    expected_torch = _torch_softmax(logits, temperature=temperature)
    expected_scipy = scipy_softmax(logits / temperature, axis=-1)
    got = softmax_temperature(logits, temperature=temperature)
    assert got == pytest.approx(expected_torch)
    assert got == pytest.approx(expected_scipy)


def test_temperature_preserves_batch_shape_vs_scipy():
    batch = np.array([[1.0, 2.0, 3.0], [3.0, 2.0, 1.0]])
    expected = scipy_softmax(batch / 2.0, axis=-1)
    got = softmax_temperature(batch, temperature=2.0)
    assert got.shape == batch.shape
    assert got == pytest.approx(expected)


def test_temperature_leaves_ranking_unchanged_vs_torch(logits):
    for temperature in (0.25, 1.0, 4.0):
        ranking = np.argsort(softmax_temperature(logits, temperature))
        assert ranking.tolist() == np.argsort(_torch_softmax(logits, temperature)).tolist()


@pytest.mark.parametrize("temperature", [0.25, 1.0, 10.0])
def test_log_softmax_matches_torch(logits_1d, logits_2d, temperature):
    for logits in (logits_1d, logits_2d):
        assert log_softmax(logits, temperature=temperature) == pytest.approx(
            _torch_log_softmax(logits, temperature=temperature)
        )


def test_log_softmax_stays_finite_like_torch():
    extreme = np.array([1e9, -1e9, 0.0])
    assert np.isfinite(log_softmax(extreme)).all()
    assert np.isfinite(_torch_log_softmax(extreme)).all()
    assert log_softmax(extreme) == pytest.approx(_torch_log_softmax(extreme))
