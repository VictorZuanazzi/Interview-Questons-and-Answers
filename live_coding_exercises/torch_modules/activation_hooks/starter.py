"""Collect intermediate activations via forward hooks."""

import torch
import torch.nn as nn


def collect_activations(
    model: nn.Module,
    x: torch.Tensor,
    layer_names: list[str],
) -> dict[str, torch.Tensor]:
    """Run one forward; return dict name -> tensor (detached cpu)."""
    raise NotImplementedError
