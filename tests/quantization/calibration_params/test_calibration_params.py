import numpy as np
import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
calibration_params = impl.calibration_params


def _quantize_affine(x, scale, zero_point, qmin=0, qmax=255):
    q = np.round(np.asarray(x, dtype=float) / scale) + zero_point
    return np.clip(q, qmin, qmax).astype(np.int32)


def _dequantize_affine(q, scale, zero_point):
    return scale * (np.asarray(q, dtype=float) - zero_point)


def test_unit_range_uint8():
    scale, zero_point = calibration_params(0.0, 1.0, qmin=0, qmax=255)
    assert scale == pytest.approx(1 / 255)
    assert zero_point == 0


def test_symmetric_range_puts_zero_point_mid_scale():
    scale, zero_point = calibration_params(-1.0, 1.0, qmin=0, qmax=255)
    assert scale == pytest.approx(2 / 255)
    assert zero_point == pytest.approx(128, abs=1)


def test_degenerate_range_still_returns_positive_scale():
    scale, _ = calibration_params(5.0, 5.0)
    assert scale > 0


def test_zero_point_stays_inside_integer_range():
    for x_min, x_max in [(-10.0, -1.0), (1.0, 10.0), (-3.0, 7.0)]:
        _, zero_point = calibration_params(x_min, x_max, qmin=0, qmax=255)
        assert 0 <= zero_point <= 255


def test_round_trip_error_within_one_step():
    scale, zero_point = calibration_params(-1.0, 1.0, qmin=0, qmax=255)
    x = np.array([-1.0, -0.5, 0.0, 0.25, 1.0])
    reconstructed = _dequantize_affine(
        _quantize_affine(x, scale, zero_point, qmin=0, qmax=255), scale, zero_point
    )
    assert np.abs(reconstructed - x).max() <= scale


def test_wider_range_gives_coarser_scale():
    narrow, _ = calibration_params(-1.0, 1.0)
    wide, _ = calibration_params(-100.0, 100.0)
    assert wide > narrow
