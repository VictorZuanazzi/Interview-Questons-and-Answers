"""Binary mask IoU and box IoU."""

import numpy as np


def binary_iou(mask_true, mask_pred):
    """Boolean or 0/1 arrays, same shape. Return IoU in [0,1]."""
    raise NotImplementedError


def box_iou(box_a, box_b):
    """Each box = (x1, y1, x2, y2). Handle no-overlap and zero-area."""
    raise NotImplementedError
