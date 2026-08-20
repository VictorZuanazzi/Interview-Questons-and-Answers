import numpy as np
import pytest

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
exponential_moving_average = impl.exponential_moving_average


def _numpy_ema(values, momentum=0.9):
    """Explicit recurrence matching the drill formula (not pandas EWM)."""
    out = []
    ema = None
    for x in np.asarray(values, dtype=float):
        ema = float(x) if ema is None else momentum * ema + (1 - momentum) * float(x)
        out.append(ema)
    return out


@pytest.mark.parametrize(
    "values, momentum",
    [
        ([10.0], 0.9),
        ([10.0, 0.0], 0.9),
        ([1.0, 2.0, 3.0, 4.0], 0.9),
        ([5.0] * 5, 0.9),
        ([0.0, 1.0], 0.1),
        ([0.0, 1.0], 0.5),
        ([0.0, 1.0], 0.99),
    ],
)
def test_matches_numpy_recurrence(values, momentum):
    assert exponential_moving_average(values, momentum=momentum) == pytest.approx(
        _numpy_ema(values, momentum=momentum)
    )


def test_output_length_matches_input():
    values = [1.0, 2.0, 3.0, 4.0]
    assert len(exponential_moving_average(values)) == len(values)


def test_state_stays_between_previous_state_and_new_value():
    for momentum in (0.1, 0.5, 0.99):
        ema = exponential_moving_average([0.0, 1.0], momentum=momentum)
        assert 0.0 <= ema[1] <= 1.0


def test_lower_momentum_tracks_new_values_faster():
    fast = exponential_moving_average([0.0, 1.0], momentum=0.1)[1]
    slow = exponential_moving_average([0.0, 1.0], momentum=0.9)[1]
    assert fast > slow
