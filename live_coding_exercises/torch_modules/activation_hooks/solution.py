"""Collect intermediate activations via forward hooks."""

import torch
import torch.nn as nn


def collect_activations(model, x, layer_names):
    """Run one forward; return dict name -> tensor (detached cpu)."""
    outs, handles = {}, []

    def make_hook(name):
        def hook(_m, _inp, out):
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
