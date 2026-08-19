"""Sliding-window Dataset over a 1D signal."""

import numpy as np
import torch
from torch.utils.data import Dataset


class SlidingWindowDataset(Dataset):
    def __init__(self, signal: np.ndarray, window: int) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, idx: int) -> torch.Tensor:
        raise NotImplementedError
