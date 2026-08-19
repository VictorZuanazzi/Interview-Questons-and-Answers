"""Greedy non-maximum suppression for axis-aligned boxes."""

import numpy as np


def nms(boxes: np.ndarray, scores: np.ndarray, iou_threshold: float = 0.5) -> list[int]:
    """boxes (N,4) xyxy, scores (N,). Return kept indices in score order."""
    raise NotImplementedError
