"""Greedy non-maximum suppression for axis-aligned boxes."""

import numpy as np


def compute_iou(box1, box2):

    max_start_x = np.maximum(box1[0], box2[0])
    max_start_y = np.maximum(box1[0], box2[0])
    min_end_x = np.minimum(box1[2], box2[2])
    min_end_y = np.minimum(box1[3], box2[3])

    intersection_x = min_end_x - max_start_x
    intersection_y = min_end_y - max_start_y

    if intersection_x <=0 or intersection_y <= 0:
        return 0.0

    intersection_area = intersection_x * intersection_y
    union_area = (box1[2] - box1[0]) * (box1[3] - box1[1]) + (box2[2] - box2[0]) * (box2[3] - box2[1])

    return 2 * intersection_area / union_area

def nms(boxes: np.ndarray, scores: np.ndarray, iou_threshold: float = 0.5) -> list[int]:
    """boxes (N,4) xyxy, scores (N,). Return kept indices in score order."""

    idx = np.argsort(scores, descending=True)
    boxes_sorted = boxes[idx]
    nms_idx = [idx[0]]

    for c, candidate in enumerate(boxes_sorted[1:]):
        for i in nms_idx:
            iou = compute_iou(boxes[i], candidate)
            if iou < iou_threshold:
                nms_idx.append(idx[c + 1])
                break
    
    return nms_idx

