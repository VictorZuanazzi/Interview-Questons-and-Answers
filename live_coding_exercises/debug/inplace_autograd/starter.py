"""Debug drill: in-place mutation of a leaf tensor."""

import torch


def broken_inplace(x: torch.Tensor) -> torch.Tensor:
    # x is a leaf that requires grad
    x += 1
    return x.sum()


def fixed_no_inplace(x: torch.Tensor) -> torch.Tensor:
    # YOUR FIX HERE
    raise NotImplementedError
