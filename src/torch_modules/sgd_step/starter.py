"""One manual SGD parameter update."""

import torch


def sgd_step(
    params: list[torch.Tensor],
    grads: list[torch.Tensor],
    lr: float,
    weight_decay: float = 0.0,
) -> list[torch.Tensor]:
    """Return updated params (list of tensors). Do not use optimizer.step."""
    raise NotImplementedError
