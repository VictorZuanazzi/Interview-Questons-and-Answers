from pathlib import Path

import numpy as np
import pytest

from live_coding_exercises.load_impl import load_impl

impl = load_impl(Path(__file__).resolve().parent)
streaming_mean_std = impl.streaming_mean_std


@pytest.mark.parametrize(
    "values",
    [
        [1.0, 2.0, 3.0],
        np.random.default_rng(0).normal(size=1000).tolist(),
        [7.0],
        [4.0] * 10,
        [1e9 + x for x in (1.0, 2.0, 3.0)],
    ],
)
def test_matches_numpy(values):
    mean, std = streaming_mean_std(values)
    assert mean == pytest.approx(np.mean(values))
    expected_std = 0.0 if len(values) < 2 else float(np.std(values, ddof=1))
    assert std == pytest.approx(expected_std, abs=1e-3 if abs(values[0]) > 1e6 else 1e-9)


def test_consumes_a_generator_in_one_pass():
    mean, std = streaming_mean_std(float(x) for x in range(5))
    values = list(range(5))
    assert mean == pytest.approx(np.mean(values))
    assert std == pytest.approx(np.std(values, ddof=1))
