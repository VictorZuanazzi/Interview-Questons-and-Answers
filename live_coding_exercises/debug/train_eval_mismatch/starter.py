"""Debug drill: train-mode dropout at inference."""

import torch
import torch.nn as nn


class DropNet(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.fc = nn.Linear(4, 2)
        self.drop = nn.Dropout(0.9)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.drop(self.fc(x))


def predict_broken(model: nn.Module, x: torch.Tensor) -> torch.Tensor:
    # BUG: model left in train mode
    return model(x)


def predict_fixed(model: nn.Module, x: torch.Tensor) -> torch.Tensor:
    # YOUR FIX HERE
    raise NotImplementedError
