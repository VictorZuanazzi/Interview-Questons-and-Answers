"""Running min/max observer for post-training quantization."""

import numpy as np


class MinMaxObserver:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def update(self, x):
        """Update running min/max over calibration batches."""
        raise NotImplementedError

    def compute_qparams(self, qmin, qmax):
        """Return (scale, zero_point)."""
        raise NotImplementedError
