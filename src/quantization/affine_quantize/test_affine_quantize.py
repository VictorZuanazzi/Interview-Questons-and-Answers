from pathlib import Path

import numpy as np
import pytest

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
quantize_affine = impl.quantize_affine
dequantize_affine = impl.dequantize_affine
sqnr_db = impl.sqnr_db

SCALE = 1 / 127


def _ref_quantize(x, scale, zero_point, qmin=-128, qmax=127):
    q = np.round(np.asarray(x, dtype=float) / scale) + zero_point
    return np.clip(q, qmin, qmax).astype(np.int32)


def _ref_dequantize(q, scale, zero_point):
    return scale * (np.asarray(q, dtype=float) - zero_point)


@pytest.fixture
def signal():
    return np.linspace(-1, 1, 100)


def test_quantize_returns_integers(signal):
    q = quantize_affine(signal, scale=SCALE, zero_point=0, qmin=-127, qmax=127)
    assert np.issubdtype(np.asarray(q).dtype, np.integer)


def test_quantize_matches_numpy_formula(signal):
    q = quantize_affine(signal, scale=SCALE, zero_point=0, qmin=-127, qmax=127)
    assert np.array_equal(q, _ref_quantize(signal, SCALE, 0, -127, 127))


def test_quantize_clips_to_representable_range():
    q = quantize_affine(np.array([-10.0, 10.0]), scale=SCALE, zero_point=0, qmin=-127, qmax=127)
    assert q.min() == -127
    assert q.max() == 127


def test_round_trip_keeps_sqnr_above_30db(signal):
    q = quantize_affine(signal, scale=SCALE, zero_point=0, qmin=-127, qmax=127)
    reconstructed = dequantize_affine(q, scale=SCALE, zero_point=0)
    assert sqnr_db(signal, reconstructed) > 30


def test_round_trip_error_bounded_by_half_a_step(signal):
    q = quantize_affine(signal, scale=SCALE, zero_point=0, qmin=-127, qmax=127)
    reconstructed = dequantize_affine(q, scale=SCALE, zero_point=0)
    assert np.abs(reconstructed - signal).max() <= SCALE / 2 + 1e-9


def test_zero_point_maps_zero_to_itself():
    q = quantize_affine(np.array([0.0]), scale=SCALE, zero_point=7, qmin=-127, qmax=127)
    assert q[0] == 7
    assert dequantize_affine(q, scale=SCALE, zero_point=7)[0] == pytest.approx(0.0)


def test_dequantize_matches_formula():
    q = np.array([-5, 0, 5])
    assert dequantize_affine(q, scale=SCALE, zero_point=2) == pytest.approx(
        _ref_dequantize(q, SCALE, 2)
    )


def test_sqnr_is_higher_for_finer_scale(signal):
    coarse = dequantize_affine(
        quantize_affine(signal, scale=1 / 7, zero_point=0, qmin=-7, qmax=7), 1 / 7, 0
    )
    fine = dequantize_affine(
        quantize_affine(signal, scale=SCALE, zero_point=0, qmin=-127, qmax=127), SCALE, 0
    )
    assert sqnr_db(signal, fine) > sqnr_db(signal, coarse)
