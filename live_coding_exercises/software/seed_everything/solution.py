"""Seed RNGs for more reproducible ML experiments."""

import random

import numpy as np
import torch


def seed_everything(seed: int):
    """Seed random, numpy, torch; set cudnn deterministic flags when available."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.use_deterministic_algorithms(True)
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
