# Neural networks and deep learning (practical)

**Time box:** 45 min
**Watch for:** nothing here is given to you. Verify every assumption you are tempted to make.

## Task

Open `interview.ipynb` and replace every `NotImplementedError`, top to bottom.

You build a binary defect detector from raw captured frames: preprocessing, the module,
the loss, the training step, the validation path, the metrics, and the operating point.

## Say out loud

1. What you checked about the data before you trained anything
2. What your model's output means, and what that forces on the loss
3. Where `zero_grad` / `backward` / `step` sit, and what each wrong order does
4. What `eval()` changes, what `no_grad()` changes, and why they are separate
5. Which number you would put in a report, and which number you would refuse to

## Practice

```bash
jupyter lab src/torch_modules/nn_dl_practical/interview.ipynb
```

`solution.py` is the reference. Reading it before you are done ends the exercise.

```bash
python src/torch_modules/nn_dl_practical/solution.py   # run the reference end to end
```
