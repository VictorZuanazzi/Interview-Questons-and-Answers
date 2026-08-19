"""Small MLP classifier returning logits."""

import torch
import torch.nn as nn


class MLPClassifier(nn.Module):
    def __init__(self, in_dim: int, hidden: int, n_classes: int) -> None:
        super().__init__()
        raise NotImplementedError

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError
