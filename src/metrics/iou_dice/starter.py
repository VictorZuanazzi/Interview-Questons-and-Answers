"""Binary mask IoU and box IoU."""

import numpy as np


def binary_iou(mask_true: np.ndarray, mask_pred: np.ndarray) -> float:
    """Boolean or 0/1 arrays, same shape. Return IoU in [0,1]."""
    raise NotImplementedError


def box_iou(
    box_a: tuple[float, float, float, float],
    box_b: tuple[float, float, float, float],
) -> float:
    """Each box = (x1, y1, x2, y2). Handle no-overlap and zero-area."""
    raise NotImplementedError
