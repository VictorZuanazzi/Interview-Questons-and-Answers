"""Small MLP classifier returning logits."""

import torch.nn as nn


class MLPClassifier(nn.Module):
    def __init__(self, in_dim, hidden, n_classes):
        super().__init__()
        raise NotImplementedError

    def forward(self, x):
        raise NotImplementedError
