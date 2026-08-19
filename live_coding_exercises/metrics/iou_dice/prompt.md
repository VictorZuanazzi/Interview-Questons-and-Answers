# IoU / Dice

**Time box:** 25–40 min  
**Watch for:** intersection clamp; union; divide-by-zero.

## Task

Implement:

1. `binary_iou(mask_true, mask_pred)` — IoU for boolean or 0/1 arrays of the same shape
2. `box_iou(box_a, box_b)` — IoU for axis-aligned boxes `(x1, y1, x2, y2)`; handle no-overlap and zero-area

## Say out loud

1. How you define union and avoid divide-by-zero
2. Why edge-touching boxes have IoU 0
3. Follow-ups: NMS uses IoU; Dice from the same primitives

## Practice

```bash
cp starter.py workspace.py
pytest live_coding_exercises/metrics/iou_dice
```
