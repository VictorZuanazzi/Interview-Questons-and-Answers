"""Binary mask IoU and box IoU."""

import numpy as np


def binary_iou(mask_true: np.ndarray, mask_pred: np.ndarray) -> float:
    """Boolean or 0/1 arrays, same shape. Return IoU in [0,1]."""
    a = np.asarray(mask_true).astype(bool)
    b = np.asarray(mask_pred).astype(bool)
    inter = np.logical_and(a, b).sum()
    union = np.logical_or(a, b).sum()
    return float(inter / union) if union > 0 else 0.0


def box_iou(
    box_a: tuple[float, float, float, float],
    box_b: tuple[float, float, float, float],
) -> float:
    """Each box = (x1, y1, x2, y2). Handle no-overlap and zero-area."""
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
    inter = iw * ih
    area_a = max(0.0, ax2 - ax1) * max(0.0, ay2 - ay1)
    area_b = max(0.0, bx2 - bx1) * max(0.0, by2 - by1)
    union = area_a + area_b - inter
    return float(inter / union) if union > 0 else 0.0
