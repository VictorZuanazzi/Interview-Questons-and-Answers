"""Running min/max observer for post-training quantization."""

import numpy as np
import torch


class MinMaxObserver:
    def __init__(self) -> None:
        self.min_val: float | None = None
        self.max_val: float | None = None

    def update(self, x: torch.Tensor) -> None:
        """Update running min/max over calibration batches."""
        x = x.detach()
        mn, mx = float(x.min()), float(x.max())
        self.min_val = mn if self.min_val is None else min(self.min_val, mn)
        self.max_val = mx if self.max_val is None else max(self.max_val, mx)

    def compute_qparams(self, qmin: int, qmax: int) -> tuple[float, int]:
        """Return (scale, zero_point)."""
        x_min, x_max = self.min_val, self.max_val
        if x_max == x_min:
            x_max = x_min + 1e-8
        scale = (x_max - x_min) / (qmax - qmin)
        zp = int(np.clip(np.round(qmin - x_min / scale), qmin, qmax))
        return float(scale), zp
