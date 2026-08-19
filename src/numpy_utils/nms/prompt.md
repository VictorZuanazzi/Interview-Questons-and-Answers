# NMS (non-maximum suppression)

**Time box:** 25–40 min  
**Watch for:** score sort order; IoU threshold; greedy suppression.

## Task

Implement `nms(boxes, scores, iou_threshold=0.5)` for `boxes (N, 4)` in xyxy format and `scores (N,)`. Return kept indices in descending score order.

## Say out loud

1. The greedy algorithm (pick best, suppress overlaps)
2. Why order of kept indices matters
3. Relation to detection post-processing

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/numpy_utils/nms
```
