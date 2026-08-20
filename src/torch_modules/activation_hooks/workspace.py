"""Collect intermediate activations via forward hooks."""

import torch
import torch.nn as nn


def collect_activations(
    model: nn.Module,
    x: torch.Tensor,
    layer_names: list[str],
) -> dict[str, torch.Tensor]:
    """Run one forward; return dict name -> tensor (detached cpu)."""

    collected_tensors = {}

    def make_hook(name: str):
        def hook(m: nn.Module, inp: tuple, out: torch.Tensor) -> None:
            collected_tensors[name] = out.detach().cpu()
        
        return hook

    modules = dict(model.named_modules())
    handlers = {}
    for name in layer_names:
        handlers[name] = modules[name].register_forward_hook(make_hook(name))

    try:
        _ = model(x)
    finally:
        for h in handlers.values():
            h.remove()

    return collected_tensors


# class Dummy(nn.Module):
#     def __init__(self):
#         super().__init__()

#         self.fc1 = nn.Linear(in_features=4, out_features=4)
#         self.act1 = nn.ReLU()
#         self.fc2 = nn.Linear(in_features=4, out_features=1)

#     def forward(self, x):
#         return self.fc2(self.act1(self.fc1(x)))

# model = Dummy()
# x = torch.randn(2, 4)
# layer_names  = ["fc1", "act1", "fc2"]

# _ = collect_activations(
#     model=model,
#     x=x,
#     layer_names=layer_names,
#     )

