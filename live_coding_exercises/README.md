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

More drills can be migrated from `live_coding.ipynb` using the same layout.

## Session checklist (25–40 min)

1. Read `prompt.md` and restate constraints out loud
2. Copy `starter.py` → `workspace.py`
3. Implement the happy path
4. Handle empties / shapes / dtypes / numerics
5. Run pytest
6. Discuss complexity and follow-ups
7. Only then open `solution.py`
