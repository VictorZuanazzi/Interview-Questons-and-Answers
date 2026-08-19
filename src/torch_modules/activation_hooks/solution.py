"""Collect intermediate activations via forward hooks."""

import torch
import torch.nn as nn


def collect_activations(
    model: nn.Module,
    x: torch.Tensor,
    layer_names: list[str],
) -> dict[str, torch.Tensor]:
    """Run one forward; return dict name -> tensor (detached cpu)."""
    outs, handles = {}, []

    def make_hook(name: str):
        def hook(_m: nn.Module, _inp: tuple, out: torch.Tensor) -> None:
            outs[name] = out.detach().cpu()

        return hook

    modules = dict(model.named_modules())
    for name in layer_names:
        handles.append(modules[name].register_forward_hook(make_hook(name)))
    try:
        model(x)
    finally:
        for h in handles:
            h.remove()
    return outs
