"""One-pass streaming mean and sample standard deviation."""

import math
from collections.abc import Iterable


def streaming_mean_std(stream: Iterable[float]) -> tuple[float, float]:
    """One-pass mean and sample std (ddof=1 if n>1 else 0)."""
    raise NotImplementedError
