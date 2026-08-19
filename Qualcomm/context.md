# Qualcomm AI Research (Amsterdam) — Interview Prep

Technical questions, hiring-process expectations, and how to prepare.

---

## Roles

Both roles are based in the **Amsterdam office**. Qualcomm is not seeking remote-based candidates.

### Senior Machine Learning Engineer

**Job area:** Engineering Group > Machine Learning Engineering

At Qualcomm AI Research, design and implement highly optimized ML solutions for generative AI, in collaboration with researchers and engineers.

**What you will do**

- Work directly with ML research teams to implement algorithms, conduct experiments, and develop research-oriented software tools.
- Work with research and product teams to bring AI models to embedded devices.
- Rapid prototyping, large-scale experimentation, fast iteration, with emphasis on code quality, maintainability, and efficiency.
- Contribute to system design and engineering so research prototypes can move toward commercial deployment.

Strong Python/PyTorch and a solid understanding of **model quantization**. C++ / Android / embedded platforms is a **big plus**.

**Requirements**

- Excellent Python, demonstrated through industry or academic experience
- PyTorch; training DNNs; generating and evaluating experimental results; improving training pipelines
- Proven experience with embedded computing and/or Android, and a solid understanding of C++
- Software development: testing, debugging, TDD
- Ability to work in a multi-site software organization

**Preferred**

- Software design/debugging plus a solid foundation in AI/ML
- Evaluating and optimizing Generative AI workflows for accuracy, performance, and other metrics
- Optimization of algebraic operations in algorithms for HW cores
- ML model optimization frameworks; quantization, pruning, etc.
- Containerization, test frameworks, static analysis, CI

**Education:** PhD or M.S. in CS, EE, robotics, or related; or B.S. with several years in related fields.

Vacancy: [Qualcomm careers](https://careers.qualcomm.com/careers/job/446716755326?hl=en-US)

### Senior Deep Learning Researcher — Physical AI / Embodied AI

**Job area:** Engineering Group > Machine Learning Researcher

Research-driven role: original research in Physical AI / Embodied Intelligence with a path to publish, plus a clear connection to real robotic systems (humanoids, dexterous manipulation).

**Areas of interest**

- RL, self-supervised learning, self-play for dexterous manipulation
- Dexterous manipulation, including tactile and force-based control
- Learning from multimodal sensory inputs (vision, proprioception, force, tactile)
- Loco-manipulation for humanoid robotics
- Vision-Language-Action (VLA) models

**Requirements**

- PhD in ML, DL, robotics, CV, or equivalent practical experience
- Deep expertise in at least one of the areas above
- Excellent Python; PyTorch / JAX
- Clean experimental pipelines and maintainable research code
- Strong publication track record in top-tier ML and/or robotics venues

**Preferred:** real-robot experiments beyond simulation; sim-to-real; humanoid or high-DoF platforms; industrial research with strong scientific output.

---

## Hiring process

Qualcomm says it uses **Eightfold AI to predict candidate–job match**, using skills in the job description and selection criteria. It may also use **automated keyword searches across the application and CV** to prioritize candidates. The automated score does **not** make the final decision, but it can influence what gets surfaced to recruiters.

Implication: the CV should make the match easy for both the matching system and a Qualcomm engineer. The vacancy's own vocabulary should appear naturally where it is truthful.

### Interview loop (Amsterdam AI Research)

The strongest Amsterdam-specific candidate report describes a virtual onsite as:

**technical presentation → Python → software architecture & CI/CD → behavioral → practical neural networks / deep learning**

Including a GitHub Actions question. Coding appears closer to **working-engineer Python and ML implementation** than LeetCode grinding. Other Qualcomm AI reports mention Python and sometimes C++ live coding, plus system/production discussions.

One report for Senior ML Engineer at Qualcomm AI Research Amsterdam covered Python, ML, CI/CD, software architecture and deployment, plus a technical presentation. Treat candidate reports as useful but noisy.

### AI-tool policy

Using LLMs to **prepare** is fine based on published policies found at the time. Qualcomm explicitly prohibits candidates from using AI tools, LLMs, bots, recording or transcription tools **during interviews or assessments**, unless Qualcomm specifically asks. Violating that can lead to disqualification.

Everything prepared here needs to become **retrievable knowledge**, not a script on a second monitor.

### Oddity in the ML Engineer vacancy

The prose says C++/Android/embedded is **“a big plus.”** The requirements then say **“proven experience with embedded computing and/or the Android platform, and a solid understanding of C++.”** Those statements are not perfectly consistent. Résumé inflation here is self-sabotage: if you get through screening, they can probe it.

---

## How to prepare

Suggested split of effort:

| Share | Area | What to practice |
|---|---|---|
| 40% | **Python live coding** | clean Python, NumPy/PyTorch, debugging, small ML functions |
| 25–30% | **ML / deep learning** | training failures, metrics, optimization, quantization, inference efficiency |
| 15–20% | **Project presentation** | defend architecture, experiments, failures, trade-offs, your contribution |
| 10% | **Software engineering / CI** | pytest, mocks, GitHub Actions, Docker, reproducibility, repo design |
| 10% | **Behavioral** | conflict, failed experiments, disagreement, mentoring, ambiguity |

C++ is worth refreshing; do **not** let it steal time from Python/ML unless they explicitly say there will be C++ coding.

**Rule:** spend at least half of prep time answering/coding, not reading.

For every question: answer verbally 2–3 minutes → struggle → write/code where relevant → only then check the solution.

### 80/20 resource plan

| Priority | Resource | Focus | Time |
|---|---|---|---:|
| 1 | [MLQuestions](https://github.com/andrewekhalel/MLQuestions) | ML/CV interview questions; answer aloud before checking | **6–8h** |
| 2 | [Chip Huyen — ML Interviews](https://huyenchip.com/ml-interviews-book/) | ML fundamentals + open-ended system/design questions | **8–10h** |
| 2.1 | [Deep Learning Interviews](https://www.interviews.ai/) | DL theory, optimization, CNNs, attention, representation learning | **6–8h** |
| 3 | [Qualcomm AI Research papers](https://www.qualcomm.com/research/artificial-intelligence/papers) | Read ~5 relevant papers: quantization, CV, GenAI, embodied AI | **5–6h** |
| 4 | [Qualcomm AIMET](https://www.qualcomm.com/developer/software/ai-model-efficiency-toolkit) | PTQ/QAT, quantization basics + one hands-on model | **6–8h** |
| 5 | [pytest fixtures](https://docs.pytest.org/en/latest/explanation/fixtures.html) + [monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) | Unit vs integration tests, fixtures, mocks | **2–3h** |
| 6 | [PyTorch reproducibility](https://docs.pytorch.org/docs/main/notes/randomness.html) | Seeds, deterministic ops, stochastic testing | **1h** |
| 7 | [GitHub Actions](https://docs.github.com/en/actions) | Workflows, PR checks, jobs, artifacts, cache | **2–3h** |
| 8 | [Docker Get Started](https://docs.docker.com/get-started/) | Images, containers, Dockerfile, layers | **2h** |
| 9 | [Python Packaging Guide](https://packaging.python.org/) | `pyproject.toml`, environments, dependencies, lockfiles | **2h** |
| 10 | [DVC](https://dvc.org/) | Data/model versioning concepts | **1–2h** |
| 11 | [LearnCpp](https://www.learncpp.com/cpp-tutorial/introduction-to-cplusplus/) | Pointers, references, RAII, STL containers, basic classes | **8–10h** |

**Total:** roughly **49–61 hours** for a strong first pass.

Suggested week-1 order:

- **Daily:** 2h ML questions + 1h live coding
- **Mon:** MLQuestions + pytest
- **Tue:** Chip Huyen + GitHub Actions
- **Wed:** Deep Learning Interviews + Docker
- **Thu:** AIMET / quantization
- **Fri:** Qualcomm papers + C++
- **Weekend / week 2:** mocks, project presentation, C++, quantization hands-on

### Qualcomm papers

Don't read 229 papers. Pick **five**.

For the ML Engineer vacancy, roughly:

- one quantization paper
- one efficient inference paper
- one generative-AI / on-device paper
- one computer-vision paper
- one paper closest to your own research

For Physical AI, swap some of those for embodied-AI / VLA work.

The objective is not “I read your paper.” It is being able to ask: “Why did you choose X rather than Y? I saw this trade-off when working on Z.”

### Quantization study path

For this vacancy, do not start with a generic course. Sequence:

**White paper → PyTorch → AIMET → Qualcomm AI Hub**

1. **Best conceptual introduction:** *A White Paper on Neural Network Quantization* — Nagel et al. Hardware-motivated explanation, then PTQ vs QAT, quantization noise, weights vs activations, low-bit inference, practical pipelines. Pay attention to: uniform affine quantization; scale and zero-point; symmetric vs asymmetric; per-tensor vs per-channel; calibration; PTQ vs QAT; why activations are usually harder than weights.
2. Implement it with the current **PyTorch quantization tutorial**.
3. Switch to **Qualcomm AIMET Quantization User Guide**.
4. Finish with a **Qualcomm AI Hub** quantization example.

You are sufficiently prepared on fundamentals when you can answer this without looking anything up:

> “I have a trained FP32 PyTorch model. I want INT8 inference on an embedded device, but I can tolerate at most a 1% accuracy drop. Walk me through what you would do, what choices you need to make, and what you would investigate if accuracy collapses.”

Bonus: actually run a PyTorch model through **AIMET or Qualcomm AI Hub**. Interview signal: curiosity and engineering behaviour without pretending to already know Snapdragon internals.

Know comfortably:

- PTQ vs QAT
- weights vs activations
- INT8 / INT4 / FP16 / FP8 trade-offs
- symmetric vs asymmetric quantization
- per-tensor vs per-channel
- scale and zero-point
- calibration datasets
- quantization error / clipping / outliers
- accuracy–latency–memory trade-offs
- why a mathematically smaller model doesn't automatically become faster on hardware
- ONNX / export / deployment issues

AIMET workflow: **model → QuantSim → calibration → evaluation → optimization → export → deployment**.

Expect questions like: Why does calibration matter? What do observers collect? Why does one layer destroy INT8 accuracy? Why might you leave certain operations unquantized? Fake quantization vs integer execution? Why might per-channel outperform per-tensor?

### Live coding style

Practice **writing useful code from scratch while somebody watches**. Not LeetCode-hard. Examples:

```python
def precision_recall(y_true, y_pred): ...
class EarlyStopping: ...
def batch_iterator(dataset, batch_size, shuffle=True): ...
```

- Implement softmax safely without `torch.softmax`
- Given probabilities and labels, find the threshold maximizing F1
- Here's a broken PyTorch training loop. Find what's wrong

Build a personal “Qualcomm 30” and solve them **without autocomplete / Copilot / ChatGPT**, ~15–25 minutes each:

1. NumPy softmax
2. Cross entropy
3. IoU
4. NMS
5. precision / recall / F1
6. confusion matrix
7. minibatch iterator
8. early stopping
9. simple linear regression
10. k-means
11. cosine similarity
12. top-k retrieval
13. simple PyTorch dataset
14. PyTorch training loop
15. gradient accumulation
16. freeze / unfreeze layers
17. custom PyTorch loss
18. checkpoint save/load
19. model parameter counting
20. simple quantizer
21. quantization scale / zero-point
22. per-channel quantization
23. image padding / resizing
24. convolution output dimensions
25. sliding-window operation
26. manipulate arrays / tensors
27. write a small class cleanly
28. unit-test one of the above
29. debug deliberately broken code
30. refactor ugly ML code

**LeetCode:** 15–25 carefully chosen Easy/Medium, not 200. Know dict/set, lists, sorting, stacks/queues, binary search, basic trees, complexity, iterators/generators. Skip the competitive-programming zoo unless interview information changes.

### PyTorch from memory

Write a training loop from memory, then expect probes:

> What changes for validation? Why `zero_grad()`? Where would you put gradient clipping? How would you accumulate gradients for four batches? What happens if I forget `model.eval()`? What does `torch.no_grad()` actually change? How would you diagnose a memory leak? What's in `model.parameters()`? Why might BatchNorm behave differently during inference?

### Project presentation

The Amsterdam report says candidates were asked to make a **technical presentation** and defend their decisions.

Expect: Why this problem formulation? Why this architecture? Alternatives? Why this loss? Why these metrics? What failed? What's the baseline? What's the ablation? How confident are you the improvement is real? Distribution shift? What was *your* contribution? What would you change now? Computational cost? Could this run on-device? How would you make it 4× faster?

Not: **Problem → architecture → results → thanks.**

Use: **Problem → why it matters → constraints → baseline → hypothesis → approach → experiment design → results → failures/limitations → what I learned → what I'd do now.**

That round can become an ML interview disguised as a presentation.

### Behavioral

Don't prepare polished corporate stories. Prepare **facts**. Have ~6 situations ready:

- technical disagreement
- failed project / experiment
- difficult debugging problem
- influencing without authority
- mentoring someone
- choosing speed vs quality
- ambiguous requirements
- something you would do differently

Use **Situation → Decision → Reasoning → Result → Learning**. Keep the situation short; interviewers care about decisions.

---

## Software engineering (interview-level)

The Amsterdam report's CI/CD / GitHub Actions / architecture questions surprised people. You don't need to become a DevOps specialist. You do need crisp vocabulary for things many ML engineers have done implicitly.

Practice answering:

> How would you design a Python repository for researchers that eventually needs to become production software?

A useful hands-on: train MNIST/CIFAR → test it → package it → GitHub Actions → Docker → reproducible training. Stack: PyTorch, pytest, ruff, `pyproject.toml`, GitHub Actions, Docker.

### Testing

- **Unit test:** one component in isolation.
- **Integration test:** components working together.
- **Smoke test:** very shallow “does the system basically run at all?”
- **Fixture:** reusable setup/teardown or test dependency.
- **Mock:** replace a dependency so you can test behavior in isolation.
- **Why not mock everything?** Then you test your mocks rather than the system.

ML examples:

- Test that preprocessing returns expected shape/dtype.
- Test that a model's forward pass works.
- Mock downloading weights rather than hitting the network.
- Integration-test preprocessing → model → postprocessing.

For stochastic tests, don't require bit-identical tensors. Test invariants, tolerances, shapes, distributions, metric bounds:

```python
assert output.shape == expected_shape
assert torch.isfinite(output).all()
assert abs(loss.item() - expected) < tolerance
```

### GitHub Actions

Hierarchy: **workflow → jobs → steps → actions/commands**

Triggers: `push`, `pull_request`, tags, path filters, `workflow_dispatch`, schedules.

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: pytest
```

**Artifacts** = outputs you want to retain/share (binaries, logs, coverage, test results).
**Cache** = expensive-to-regenerate inputs (dependencies, intermediate build outputs).

> PyTorch wheel downloaded repeatedly → **cache**
> Quantized ONNX model generated by the pipeline → **artifact**

### Docker

**Image:** immutable template. **Container:** running instance. **Dockerfile:** instructions.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install .
COPY src ./src
CMD ["python", "-m", "my_project"]
```

Copy dependency files before source so Docker layers cache dependency installation when source changes.

### Dependencies and versioning

`pyproject.toml` = project metadata / dependency **constraints**.
`uv.lock` / `poetry.lock` / `requirements.txt` = **exact resolved environment**.

Don't put large datasets or weights in Git. Version references/metadata alongside code; store artifacts in object storage or a registry so an experiment traces back to code + data + config + model.

**Formatter** (`black`, `ruff format`) vs **linter** (`ruff`) vs **type checker** (`mypy`, `pyright`) vs **tests**.

Typical CI: format check → lint → type checking → unit tests → integration tests → build/package.

### Research → production repo

```text
project/
├── pyproject.toml
├── README.md
├── src/project/{data,models,training,inference,evaluation}/
├── tests/{unit,integration}/
├── configs/
├── scripts/
├── notebooks/
├── docker/
└── .github/workflows/
```

Defend: reusable logic in `src/`, not notebooks; config separate from code; clear interfaces; tests at important boundaries; environment definitions committed; CI on PRs; **don't prematurely productionize research**.

---

## Technical questions

Interview-style questions with sharpened answers. Practice answering first, then check.

### Q1. INT8 PTQ drops accuracy 92% → 84%. Diagnose it.

**Principle:** first locate the error; then explain the error; then fix it. Don't jump to “maybe clipping/scaling is wrong.”

1. **Confirm the degradation is really caused by quantization** — same preprocessing, eval set, model mode, metric implementation.
2. **Localize the damage** — compare FP32 vs quantized layer by layer: activations, output distributions, cosine similarity / MSE, saturation, SQNR.
3. **Identify sensitive layers** — maybe 95% of layers are fine and one attention block / first conv / final classifier is destroyed.
4. **Only then ask why** — clipping, activation outliers, poor calibration set, per-tensor where per-channel is needed, INT8-sensitive op, bad scale propagation, unsupported op fallback.
5. **Then intervene** — change calibration, alter clipping, per-channel, keep one layer in FP16/FP32, QAT.

**Localize a layer:** run representative (not random) inputs through both models. To separate local sensitivity from error propagation, inject the FP32 activation into each quantized layer and compare against the FP32 layer output.

Quantization is **per tensor or per channel**; what matters is the distribution **within that tensor/channel**, not relative to other layers. BatchNorm is often folded into Conv at inference. For attention, the bigger problem is often **activation outliers and highly non-uniform ranges** in Q/K/V or attention outputs, not softmax alone.

**Affine vs symmetric:** affine quantization does **not** necessarily map the largest absolute value to `-128/127`; that describes a symmetric scheme. Zero is represented exactly via the **zero-point**; you don't generally “add 128 at the end.” Signed `int8` is commonly used directly. In PTQ, scales usually come from **calibration statistics/observers**.

Crisp answer:

> I'd first compare FP32 and quantized activations on representative data. To distinguish accumulated error from intrinsic layer sensitivity, I'd inject the FP32 activation into each quantized layer and compare its output against the FP32 layer output using MSE, cosine similarity, SQNR, and saturation rate. That lets me rank sensitive layers. I'd then inspect whether the issue comes from outliers, poor calibration, per-tensor scaling where per-channel is needed, or particularly sensitive operations.

#### Comparison metrics

- **MSE** — average squared difference. Lower is better. Absolute numerical distortion.
- **MAE** — mean absolute error.
- **Cosine similarity** — whether two activation vectors point in the same direction. `1` ≈ same direction.
- **SQNR** — Signal-to-Quantization-Noise **Ratio**: \(10\log_{10}\|x\|^2 / \|x-\hat{x}\|^2\). Higher is better.
- **Saturation rate** — fraction of values outside the chosen range (clipped).
- Also: mean shift, variance/std change, max absolute error, relative / normalized error.

Don't compare raw MSE across layers blindly. A layer with activations around `100` will have larger MSE than one around `0.01`. Use SQNR, relative error, or normalized MSE for cross-layer ranking. Look for the **first** layer where metrics deteriorate, not just the largest absolute MSE. A layer can have low MSE but still hurt accuracy if the error is in a sensitive direction.

#### Per-channel vs per-tensor

Per-channel helps when channel-wise distributions differ: each channel gets its own scale instead of one global scale dominated by the widest-range channel. **Bit width is usually still shared.**

Costs: more scale/zero-point metadata; more complicated kernels; potentially worse hardware efficiency; not every backend supports every scheme.

> Per-channel quantization helps when channel-wise distributions differ significantly, because each channel gets its own scale instead of sharing one global scale. The trade-off is extra metadata and potentially more complex or less efficient hardware execution.

**Why per-channel weights but often per-tensor activations?** Weights are static; scales can be computed offline and stored. Activations are input-dependent; per-channel activation quantization adds runtime overhead, and ranges vary across samples. Hardware often supports **per-tensor activations + per-channel weights** efficiently.

#### PTQ vs QAT

**PTQ:** quantize a trained FP32 model using calibration, no (or minimal) retraining. Fast, cheaper, often enough if the drop is small.

**QAT:** simulate quantization during training (fake quant) so the model adapts to quantization noise. Use when PTQ loses too much accuracy, or for lower bit-widths.

#### Calibration methods (quantization, not probability calibration)

Quantization calibration = estimate ranges/statistics (scale, zero-point, clip thresholds). Classifier calibration = whether `0.7` means ~70% true positive rate. Same word, different problem.

- **Min–max:** observed min/max. Simple; sensitive to outliers.
- **Percentile:** e.g. 99.9th percentile. Sacrifices rare extremes for better resolution.
- **MSE-based:** range that minimizes reconstruction error.
- **SQNR-based:** maximize signal-to-quantization-noise ratio.
- **KL / entropy:** preserve the overall distribution.
- **Moving-average min–max:** less noisy over batches.

The **calibration dataset** matters enormously. Be fluent on min-max, percentile, and MSE/SQNR.

### Skip connections: add vs concat

**Elementwise addition is generally more hardware-friendly than concatenation**, assuming compatible shapes.

- Addition reads two tensors and writes one of the **same shape**.
- Concatenation creates a **larger** output; the next layer processes more channels. Cost propagates.
- Additions are easier to **fuse** into neighboring Conv/Linear kernels.

A projection (`1×1` conv or linear) can align shapes, but **the projection itself costs compute and memory**. Concatenation is not inherently bad architecture. Think in terms of downstream tensor size, memory traffic, kernel fusion, and target-hardware behavior.

Operations to be suspicious of on embedded inference: concat/split/reshape with copies; transpose/permute/layout conversions; large elementwise chains; normalization; softmax; attention; dynamic shapes / control flow; unsupported ops; large upsampling / feature maps; repeated device transfers.

> Don't count FLOPs alone. Ask how many bytes must move, how large the intermediate tensors become, whether the operation maps efficiently to the target accelerator, and whether it can be fused.

### Q2. Low-FLOP block is a large fraction of inference time. Why?

FLOPs measure arithmetic work, not total execution cost. On embedded hardware, data movement and overhead can dominate.

Checklist: **memory → transfers → launches → fusion → kernels → layouts → synchronization → dynamic shapes → utilization**

- **Memory-bandwidth bound** — little math, large read/write. Elementwise ops, normalization, copies.
- **CPU ↔ accelerator transfers** — unsupported ops bounce to CPU.
- **Kernel launch overhead** — many tiny ops; 20 elementwise kernels can beat one fused kernel.
- **Poor operator support** — generic slow kernel on the accelerator.
- **Lack of fusion** — `Linear → bias → activation → norm` as several kernels, rewriting intermediates.
- **Tensor layout conversions** — `transpose`/`permute` or incompatible layouts force copies.
- **Synchronization** — wait for previous async work; profiler may blame an innocent op.
- **Dynamic shapes** — block specialized kernels, static memory planning, fusion; may reallocate. Not necessarily *large* allocations.
- **Runtime memory allocation** — alloc/free during inference vs preallocated buffers.
- **Low parallelism / poor utilization** — awkward shapes (e.g. `13×17` GEMM) don't fill the accelerator.

> Latency ≈ compute + memory movement + launch/runtime overhead + synchronization + hardware inefficiency.

If someone says “this op has almost no FLOPs, why is it slow?”, first reaction: **then FLOPs probably aren't the bottleneck.**

### Q3. Accurate in PyTorch; after ONNX export, predictions differ.

Separate **export success** from **semantic correctness**. Macro to micro.

1. Verify identical inputs, preprocessing, model mode, and postprocessing.
2. Run PyTorch and ONNX Runtime on the **same hardware/precision**.
3. Compare final outputs numerically.
4. Compare intermediate tensors layer-by-layer.
5. Check exporter warnings, unsupported/custom ops, operator versions, padding/broadcast semantics.
6. Test FP32 vs reduced precision.
7. Only then compare across target hardware/runtime.

Treat bias/variance of the error as a **clue**, not a diagnosis. A systematic shift could be preprocessing, normalization, precision, broadcasting, padding, or operator differences.

If workstation PyTorch and ONNX match but the **embedded target** diverges: don't anchor only on kernels. Check precision mode (FP16/INT8), fused kernels, operator fallback, layout conversions, whether the target runtime is using the **same graph** or applied optimizations. Compare intermediate activations **on the target** against workstation ONNX to find the first point of divergence.

> Once I find the first layer where outputs diverge materially, I'd determine whether the cause is reduced precision, a different kernel implementation, graph fusion, layout conversion, or unsupported-op fallback.

Tiny local discrepancies can **compound** through the network. CUDA kernel-selection heuristics can produce ~1e-4 differences across GPU architectures.

### Q4. Research repo is notebooks, globals, hard-coded paths. Make it usable by five researchers without killing experimentation. What first? What *not* yet?

1. Identify the stable core used by multiple researchers.
2. Extract shared preprocessing/training/evaluation from notebooks into **named modules** (`data/`, `models/`, `training/`, `evaluation/`) — not a junk-drawer `utils`.
3. Centralize experiment configuration. Machine-specific paths: env vars or a local ignored config, not committed secrets.
4. Add tests around high-risk shared components **before** major refactors.
5. Minimal package structure and reproducible environment.
6. Lightweight CI: lint + unit tests.
7. Leave exploratory notebooks and unstable ideas alone.

Don't deprecate aggressively without usage evidence; hidden dependencies are common. Keep researchers in the loop; improve *their* workflow first (e.g. scattered hyperparameters) to get buy-in.

> I wouldn't build elaborate service abstractions, deployment infrastructure, comprehensive integration tests, or rigid APIs around experimental code that may disappear next week.

#### CI on every PR vs not

**Every PR (minutes, not hours):** formatting, lint, static analysis, unit tests, cheap integration/smoke tests, import/package sanity. Checksums when the PR can break those artifacts.

**Not every PR:** full training, large validation, GPU profiling, hardware-specific tests, exhaustive E2E, large artifact generation, publishing. Those belong on **main / nightly / release / dedicated hardware**.

> Slow CI gets bypassed.

### Q5. Unit vs integration vs smoke test in an ML codebase

- **Unit:** one function in isolation. Example: preprocessing yields expected range and shape.
- **Integration:** several components together. Example: dataloader → preprocess → forward → postprocess yields valid predictions.
- **Smoke:** shallow “does it run?” Example: train 2 batches, save checkpoint, reload, infer 1 sample, no crash/NaNs.

Integration tests are broader than HTTP APIs.

#### Mocks

Use mocks to isolate from slow, nondeterministic, or external dependencies (APIs, filesystem, model downloads). **Mock the dependency, not the data** — if the function accepts an array, construct a tiny tensor.

Too much mocking: you test assumptions instead of reality; tests couple to implementation details; you miss integration bugs; mocks can lie.

> Mocks make unit tests faster and clearer. Complement them with integration tests that verify real collaboration.

### Q6. Training isn't reproducible even with `torch.manual_seed(42)`

- Seed **Python, NumPy, and PyTorch** (and sklearn if used).
- **DataLoader workers** need their own seeds/generators.
- **cuDNN / CUDA** may pick nondeterministic algorithms.
- Data order / augmentation RNGs.
- Floating-point reduction order can compound.
- Different hardware / library versions can still differ.

```python
torch.use_deterministic_algorithms(True)
torch.backends.cudnn.benchmark = False
```

> I'd seed Python, NumPy, and PyTorch; control DataLoader worker seeds and shuffling; enable deterministic algorithms where possible; disable benchmarking that selects different kernels; and pin the software/hardware environment. Even then, I wouldn't promise bitwise reproducibility across different GPUs or PyTorch/CUDA versions.

**Why can determinism be slower?** Faster kernels often use parallelism or atomics whose order isn't guaranteed. Enforcing determinism may mean more synchronization, stricter ordering, or slower fallbacks.

### Q7. Fewer FLOPs, slower on GPU. How?

Same failure modes as Q2: poor kernels, lack of fusion, CPU–GPU transfers, sync, allocation, layout conversions, memory-bandwidth limits, poor utilization.

A `permute` can be a view; a later op requiring contiguous memory may trigger the real copy.

### Q8. Latency vs throughput

- **Latency** = time for one request/sample.
- **Throughput** = samples completed per unit time.

Batching often **increases throughput** (better GPU utilization) and **increases latency** (each request waits for the batch).

### Q9. Why does larger batch help throughput, then stop?

More parallel work; amortizes launch and transfer overhead. Gains often **plateau before OOM** because compute or memory bandwidth is already saturated. Then larger batches mainly increase latency and memory. GEMMs/convs benefit more than memory-bound ops. Eventually OOM.

### Q10. Fewer parameters, more inference memory?

**Inference memory ≈ weights + activations + workspace + runtime overhead.**

A smaller-weight model can keep huge feature maps, concat/attention intermediates, skip-connection tensors, FP32 vs INT8, fragmentation.

Parameter count is **not** a reliable proxy for peak inference memory.

### Q11. Train loss ↓, val loss ↑ after epoch 12, val accuracy almost flat

Classic **overfitting**. Rising val loss with **flat accuracy** can mean the model is becoming **more confidently wrong**; cross-entropy sees that even if argmax doesn't.

First: verify split and **data leakage**. Then: weight decay, stronger augmentation, early stopping, reduce effective capacity.

Corrections: dropout's main cost is noisier optimization, not huge compute. Normalization is not a substitute for dropout; BatchNorm's primary job is optimization/stability. The term is **L2/L1 regularization / weight decay**, not “weight normalization.”

### Q12. 1% positives, 99% accuracy

A trivial all-negative classifier already gets 99% accuracy.

**Accuracy** = \((TP + TN)/(TP+TN+FP+FN)\)
**Precision** = \(TP / (TP+FP)\)
**Recall** = \(TP / (TP+FN)\)
**F1** = **harmonic** mean: \(2PR/(P+R)\), not geometric.

Also mention **PR-AUC**. ROC-AUC can look deceptively good under heavy imbalance.

### Q13. 95% recall, 20% precision

The model finds most positives but also flags many false positives (over-predicting the positive class). You can **raise the decision threshold** without retraining to trade recall for precision (or lower it the other way). Choose the operating point from application costs.

---

## Extra ML / systems questions to drill

- Why can validation loss increase while accuracy stays constant?
- Model trains on one GPU but changes output on another. Diagnose it.
- Why can fewer FLOPs produce higher latency?
- PTQ loses 8% accuracy. Diagnose it.
- Why does BatchNorm behave differently at inference?
- Adam vs SGD — when might SGD generalize better?
- What happens when the learning rate is too high / too low?
- Why might mixed precision training become unstable?
- How would you detect data leakage?
- Your positive class is 0.1%. How do you train and evaluate?

---

## Short explanations

### TensorRT

NVIDIA’s inference optimization/runtime that compiles trained networks into highly optimized GPU engines using kernel fusion, precision reduction, and hardware-specific graph optimization.

### FlashAttention

Exact attention, computed more efficiently by reducing **memory movement**, not by changing the formula \(\mathrm{softmax}(QK^T)V\).

The \(N \times N\) attention matrix is huge; writing it to GPU memory and reading it back is expensive. FlashAttention tiles \(Q,K,V\) in on-chip SRAM, computes softmax incrementally, combines with \(V\), and writes only the final output.

> Same math, much less memory traffic.

It does **not** change the \(O(N^2)\) arithmetic complexity; it improves memory complexity and hardware efficiency.

### GIL

The **Global Interpreter Lock** in CPython allows only **one thread at a time to execute Python bytecode**.

- Threads still help **I/O-bound** work (GIL released while waiting).
- Many native libraries (NumPy, PyTorch) release the GIL during C/C++/CUDA work.
- True parallelism for **pure Python CPU** work usually means **multiprocessing**.

### Concurrent execution in Python

- **Threads** — I/O-bound; limited by GIL for pure Python CPU.
- **Processes** — CPU-bound Python; each process has its own interpreter/GIL.
- **Asyncio** — high-concurrency I/O; cooperative, usually one thread.
- **Native / GPU** — much of ML parallelism happens here.

### Image decode: threads vs processes vs GPU

If compressed bytes are already in memory, decompression is `imdecode`, not `imread` (which also does file I/O).

**Threads first** if a native decoder (OpenCV/libjpeg) **releases the GIL**. Lower overhead than processes.

**Processes** if the decoder holds the GIL or preprocessing is pure-Python CPU-bound. Downside: serialize/copy large decoded images back to the parent; a 1 MB JPEG can become 20–50 MB uncompressed.

**GPU-native decode** (nvJPEG, DALI) if decode throughput is the bottleneck.

Typical GPU pipeline: **threaded CPU decode → pinned host memory → asynchronous H→D copy**.

`DataLoader(num_workers=N)` uses **processes**, which is why it is the usual PyTorch starting point.

```python
from concurrent.futures import ThreadPoolExecutor
import cv2
import numpy as np

def decompress_jpeg(jpeg_bytes: bytes):
    buf = np.frombuffer(jpeg_bytes, dtype=np.uint8)
    return cv2.imdecode(buf, cv2.IMREAD_COLOR)

with ThreadPoolExecutor(max_workers=4) as pool:
    decoded_images = list(pool.map(decompress_jpeg, compressed_images))
```

Same pattern with `ProcessPoolExecutor` if you need processes.

PyTorch training loop pattern:

```python
loader = torch.utils.data.DataLoader(
    dataset, batch_size=32, num_workers=4, pin_memory=True
)
for images, labels in loader:
    images = images.cuda(non_blocking=True)
    labels = labels.cuda(non_blocking=True)
    output = model(images)
```

---

## Live coding #1 — precision / recall / F1

Implement without scikit-learn. Handle edge cases (divide-by-zero).

```python
def precision_recall_f1(y_true, y_pred):
    """
    y_true and y_pred are lists of 0/1 integers.
    Return: precision, recall, f1
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    tp = ((y_true == 1) & (y_pred == 1)).sum()
    fp = ((y_true == 0) & (y_pred == 1)).sum()
    fn = ((y_true == 1) & (y_pred == 0)).sum()

    precision = tp / (tp + fp) if tp + fp > 0 else 0.0
    recall = tp / (tp + fn) if tp + fn > 0 else 0.0

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall > 0
        else 0.0
    )

    return precision, recall, f1
```

Traps that show up in live coding:

- `tp = (y_true == (y_pred == 1)).sum()` is wrong; you want `(y_true == 1) & (y_pred == 1)`.
- `tp / tp + fp` is `(tp / tp) + fp` — **parentheses**.
- F1 is \(2PR/(P+R)\), not \(2(P+R)/(PR)\) and not \(1/(1/P + 1/R)\) (that last one is missing the factor 2, i.e. it is half of F1).
- Avoid `~y_true` on integer arrays: `~0 == -1`, `~1 == -2`. Write `y_true == 0` explicitly.
- Don't leave a second experimental formula that overwrites the correct one.
- Don't compute `tn` if you don't use it.
