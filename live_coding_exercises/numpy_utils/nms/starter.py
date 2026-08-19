"""Greedy non-maximum suppression for axis-aligned boxes."""

import numpy as np


def nms(boxes, scores, iou_threshold=0.5):
    """boxes (N,4) xyxy, scores (N,). Return kept indices in score order."""
    raise NotImplementedError
