"""Collect intermediate activations via forward hooks."""

import torch
import torch.nn as nn


def collect_activations(model, x, layer_names):
    """Run one forward; return dict name -> tensor (detached cpu)."""
    raise NotImplementedError
