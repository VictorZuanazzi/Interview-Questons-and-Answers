"""One-pass streaming mean and sample standard deviation."""

import math


def streaming_mean_std(stream):
    """One-pass mean and sample std (ddof=1 if n>1 else 0)."""
    n, mean, M2 = 0, 0.0, 0.0
    for x in stream:
        n += 1
        delta = x - mean
        mean += delta / n
        M2 += delta * (x - mean)
    if n < 2:
        return mean, 0.0
    return mean, math.sqrt(M2 / (n - 1))
