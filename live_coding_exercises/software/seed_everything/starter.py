"""Seed RNGs for more reproducible ML experiments."""

import random

import numpy as np
import torch


def seed_everything(seed: int):
    """Seed random, numpy, torch; set cudnn deterministic flags when available."""
    raise NotImplementedError
