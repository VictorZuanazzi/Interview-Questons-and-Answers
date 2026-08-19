"""One manual SGD parameter update."""

import torch


def sgd_step(params, grads, lr, weight_decay=0.0):
    """Return updated params (list of tensors). Do not use optimizer.step."""
    raise NotImplementedError
