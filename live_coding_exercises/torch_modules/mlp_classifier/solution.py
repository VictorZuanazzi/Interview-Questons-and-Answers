"""Small MLP classifier returning logits."""

import torch
import torch.nn as nn


class MLPClassifier(nn.Module):
    def __init__(self, in_dim: int, hidden: int, n_classes: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, n_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)
