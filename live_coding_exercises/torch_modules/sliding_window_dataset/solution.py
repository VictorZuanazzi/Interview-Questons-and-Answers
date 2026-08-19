"""Sliding-window Dataset over a 1D signal."""

import numpy as np
import torch
from torch.utils.data import Dataset


class SlidingWindowDataset(Dataset):
    def __init__(self, signal, window):
        self.signal = np.asarray(signal)
        self.window = window

    def __len__(self):
        return max(0, len(self.signal) - self.window + 1)

    def __getitem__(self, idx):
        return torch.as_tensor(self.signal[idx: idx + self.window])
