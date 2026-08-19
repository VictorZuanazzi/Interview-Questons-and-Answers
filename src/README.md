# Live coding exercises

Repeatable drills without notebooks. Each exercise is a small folder:

```text
metrics/softmax/
  prompt.md      # problem + what to say out loud
  starter.py     # stubs only — source of truth for a fresh attempt
  workspace.py   # your attempt (gitignored; copy from starter)
  solution.py    # reference implementation
  test_*.py      # pytest judge
```

## Practice a drill

```bash
cd /path/to/Interview-Questons-and-Answers
python -m venv .venv && source .venv/bin/activate
pip install -r live_coding_exercises/requirements.txt

cp live_coding_exercises/metrics/softmax/starter.py \
   live_coding_exercises/metrics/softmax/workspace.py

# implement in workspace.py, then:
pytest live_coding_exercises/metrics/softmax
```

Reset and try again:

```bash
cp live_coding_exercises/metrics/softmax/starter.py \
   live_coding_exercises/metrics/softmax/workspace.py
```

## How tests choose your code

- If `workspace.py` exists → tests import it (practice mode)
- If not → tests import `solution.py` (CI / check references)
- Force the reference anytime: `USE_SOLUTION=1 pytest live_coding_exercises/metrics/softmax`

## Available drills

| Drill | Path |
|---|---|
| Precision / Recall / F1 | `metrics/precision_recall_f1/` |
| Softmax (+ temperature, log-softmax) | `metrics/softmax/` |
| Cross-entropy (binary + multiclass) | `metrics/cross_entropy/` |
| Confusion-matrix primitives | `metrics/confusion_matrix/` |
| Top-k accuracy | `metrics/top_k_accuracy/` |
| IoU (mask + box) | `metrics/iou_dice/` |
| Exponential moving average | `metrics/ema/` |
| Affine quantize / dequantize | `quantization/affine_quantize/` |
| Calibration params from range | `quantization/calibration_params/` |
| MinMax PTQ observer | `quantization/minmax_observer/` |
| Tiny MLPClassifier | `torch_modules/mlp_classifier/` |
| Manual SGD step | `torch_modules/sgd_step/` |
| Sliding-window Dataset | `torch_modules/sliding_window_dataset/` |
| Causal / padding masks | `torch_modules/attention_masks/` |
| Activation dump (hooks) | `torch_modules/activation_hooks/` |
| Pairwise L2 distances | `numpy_utils/pairwise_l2/` |
| One-hot + gather | `numpy_utils/one_hot_gather/` |
| NMS | `numpy_utils/nms/` |
| Streaming mean/std (Welford) | `numpy_utils/welford/` |
| Concurrent JPEG decode | `numpy_utils/concurrent_jpeg/` |
| Debug: broken F1 | `debug/broken_f1/` |
| Debug: softmax overflow | `debug/softmax_overflow/` |
| Debug: train/eval mismatch | `debug/train_eval_mismatch/` |
| Debug: in-place autograd | `debug/inplace_autograd/` |
| Debug: attention scores | `debug/attention_scores/` |
| Deep config merge | `software/deep_merge/` |
| Seed everything | `software/seed_everything/` |
| Write the tests (pytest) | `software/write_tests/` |
| Artifact path helper | `software/artifact_path/` |
| Occupancy grid | `spatial/occupancy_grid/` |
| Voxel downsample | `spatial/voxel_downsample/` |

## Session checklist (25–40 min)

1. Read `prompt.md` and restate constraints out loud
2. Copy `starter.py` → `workspace.py`
3. Implement the happy path
4. Handle empties / shapes / dtypes / numerics
5. Run pytest
6. Discuss complexity and follow-ups
7. Only then open `solution.py`
