from pathlib import Path

import numpy as np
import pytest
import torch

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
MinMaxObserver = impl.MinMaxObserver


def _quantize_affine(x, scale, zero_point, qmin=0, qmax=255):
    q = np.round(np.asarray(x, dtype=float) / scale) + zero_point
    return np.clip(q, qmin, qmax).astype(np.int32)


def _dequantize_affine(q, scale, zero_point):
    return scale * (np.asarray(q, dtype=float) - zero_point)


@pytest.fixture
def observer():
    obs = MinMaxObserver()
    obs.update(torch.tensor([-1.0, 0.5]))
    obs.update(torch.tensor([2.0]))
    return obs


def test_tracks_running_min_and_max(observer):
    assert float(observer.min_val) == pytest.approx(-1.0)
    assert float(observer.max_val) == pytest.approx(2.0)


def test_narrower_batch_does_not_shrink_the_range(observer):
    observer.update(torch.tensor([0.0]))
    assert float(observer.min_val) == pytest.approx(-1.0)
    assert float(observer.max_val) == pytest.approx(2.0)


def test_qparams_are_valid(observer):
    scale, zero_point = observer.compute_qparams(0, 255)
    assert scale > 0
    assert 0 <= zero_point <= 255


def test_is_order_invariant():
    forward, backward = MinMaxObserver(), MinMaxObserver()
    batches = [torch.tensor([-1.0, 0.5]), torch.tensor([2.0])]
    for batch in batches:
        forward.update(batch)
    for batch in reversed(batches):
        backward.update(batch)
    assert forward.compute_qparams(0, 255) == pytest.approx(backward.compute_qparams(0, 255))


def test_calibrated_range_covers_observed_values(observer):
    scale, zero_point = observer.compute_qparams(0, 255)
    values = np.array([-1.0, 0.0, 2.0])
    reconstructed = _dequantize_affine(
        _quantize_affine(values, scale, zero_point, qmin=0, qmax=255), scale, zero_point
    )
    assert np.abs(reconstructed - values).max() <= scale
