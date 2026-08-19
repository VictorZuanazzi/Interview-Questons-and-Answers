"""Debug drill: train-mode dropout at inference."""

import torch
import torch.nn as nn


class DropNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(4, 2)
        self.drop = nn.Dropout(0.9)

    def forward(self, x):
        return self.drop(self.fc(x))


def predict_broken(model, x):
    # BUG: model left in train mode
    return model(x)


def predict_fixed(model, x):
    # YOUR FIX HERE
    raise NotImplementedError
