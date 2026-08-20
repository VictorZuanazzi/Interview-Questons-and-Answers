import numpy as np
import pytest
import torch
from torchvision.ops import box_iou as tv_box_iou
from torchvision.ops import nms as tv_nms

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
nms = impl.nms

BOXES = np.array(
    [
        [0.0, 0.0, 2.0, 2.0],
        [0.5, 0.5, 2.5, 2.5],
        [5.0, 5.0, 7.0, 7.0],
    ]
)
SCORES = np.array([0.9, 0.8, 0.7])


def _tv(boxes, scores, iou_threshold):
    return tv_nms(
        torch.as_tensor(boxes, dtype=torch.float32),
        torch.as_tensor(scores, dtype=torch.float32),
        iou_threshold,
    ).tolist()


@pytest.mark.parametrize(
    "iou_threshold",
    [0.3, 0.5, 0.99],
)
def test_matches_torchvision_nms(iou_threshold):
    assert list(nms(BOXES, SCORES, iou_threshold=iou_threshold)) == _tv(
        BOXES, SCORES, iou_threshold
    )


def test_returns_indices_in_descending_score_order():
    scores = np.array([0.1, 0.5, 0.9])
    kept = list(nms(BOXES, scores, iou_threshold=0.99))
    assert kept == sorted(kept, key=lambda i: -scores[i])
    assert kept == _tv(BOXES, scores, 0.99)


def test_single_box_is_always_kept():
    assert list(nms(BOXES[:1], SCORES[:1], iou_threshold=0.5)) == [0]


def test_identical_boxes_collapse_to_one():
    duplicated = np.repeat(BOXES[:1], 3, axis=0)
    scores = np.array([0.9, 0.8, 0.7])
    assert list(nms(duplicated, scores, iou_threshold=0.5)) == _tv(
        duplicated, scores, 0.5
    )


def test_kept_boxes_do_not_overlap_above_threshold():
    threshold = 0.3
    kept = list(nms(BOXES, SCORES, iou_threshold=threshold))
    boxes_t = torch.as_tensor(BOXES, dtype=torch.float32)
    for i, first in enumerate(kept):
        for second in kept[i + 1 :]:
            iou = tv_box_iou(boxes_t[first : first + 1], boxes_t[second : second + 1])[
                0, 0
            ].item()
            assert iou <= threshold
