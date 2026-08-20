import numpy as np
import pytest
import torch
from sklearn.metrics import jaccard_score
from torchvision.ops import box_iou as tv_box_iou

from src.load_impl import load_impl_for_test

impl = load_impl_for_test(__file__)
binary_iou = impl.binary_iou
box_iou = impl.box_iou


@pytest.mark.parametrize(
    "mask_true, mask_pred",
    [
        ([1, 1, 0, 0], [1, 0, 1, 0]),
        ([1, 0, 1, 1], [1, 0, 1, 1]),
        ([1, 1, 0, 0], [0, 0, 1, 1]),
        ([0, 0], [0, 0]),
        ([1, 1, 1, 0], [1, 0, 1, 0]),
    ],
)
def test_binary_iou_matches_sklearn(mask_true, mask_pred):
    expected = jaccard_score(mask_true, mask_pred, zero_division=0.0)
    assert binary_iou(mask_true, mask_pred) == pytest.approx(expected)


@pytest.mark.parametrize(
    "box_a, box_b",
    [
        ((0, 0, 2, 2), (1, 1, 3, 3)),
        ((0, 0, 1, 1), (2, 2, 3, 3)),
        ((0, 0, 2, 2), (0, 0, 2, 2)),
        ((0, 0, 4, 4), (1, 1, 2, 2)),
        ((0, 0, 1, 1), (1, 0, 2, 1)),
    ],
)
def test_box_iou_matches_torchvision(box_a, box_b):
    expected = tv_box_iou(
        torch.tensor([box_a], dtype=torch.float32),
        torch.tensor([box_b], dtype=torch.float32),
    )[0, 0].item()
    assert box_iou(box_a, box_b) == pytest.approx(expected, abs=1e-6)


def test_box_iou_zero_area_is_zero():
    # torchvision.ops.box_iou returns NaN for 0/0; this drill uses 0.0
    assert box_iou((0, 0, 0, 0), (0, 0, 0, 0)) == pytest.approx(0.0)


def test_box_iou_is_symmetric():
    box_a, box_b = (0, 0, 2, 2), (1, 1, 3, 3)
    assert box_iou(box_a, box_b) == pytest.approx(box_iou(box_b, box_a))
