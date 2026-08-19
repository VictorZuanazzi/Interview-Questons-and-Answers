"""Running min/max observer for post-training quantization."""

import numpy as np
import torch


class MinMaxObserver:
    def __init__(self) -> None:
        self.min_val: float | None = None
        self.max_val: float | None = None

    def update(self, x: torch.Tensor) -> None:
        """Update running min/max over calibration batches."""
        raise NotImplementedError

    def compute_qparams(self, qmin: int, qmax: int) -> tuple[float, int]:
        """Return (scale, zero_point)."""
        raise NotImplementedError
