# Qualcomm interview prep

## Quantization / model optimization

1. You have an FP32 PyTorch model and want INT8 inference on an embedded device with ≤1% accuracy loss. Walk me through your choices and how you would debug an accuracy collapse.
2. Can I assume affine quantization and clipping?
3. How would you determine which specific layer or operation is responsible for most of the quantization accuracy degradation?
4. What would you measure when comparing FP32 and quantized activations?
5. Define MSE, cosine similarity, SQNR, and saturation rate.
6. A Linear layer has poor SQNR under per-tensor INT8 quantization. Why might per-channel quantization help, and what does it cost?
7. Why is per-channel quantization commonly used for weights while activations are often per-tensor?
8. What is the difference between post-training quantization and quantization-aware training, and when would you choose each?
9. What are the most common quantization calibration methods?
10. Is quantization calibration different from classifier probability calibration?
11. Why does calibration matter?
12. What do quantization observers collect?
13. Why can one layer destroy INT8 accuracy?
14. Why might you deliberately leave some operations unquantized?
15. What is the difference between fake quantization and actual integer execution?
16. Why might per-channel quantization outperform per-tensor quantization?
17. PTQ causes an 8% accuracy loss. Diagnose it.
18. Could you quantize this model/project?

## Hardware efficiency / inference

1. Which forward-pass operations are undesirable from a memory/runtime perspective?
2. For skip connections, which is more hardware-friendly: addition or concatenation?
3. Is it reasonable to use additive residuals and projections instead of concatenation to reduce compute/memory?
4. A block has very few FLOPs but consumes a large fraction of inference time. Why?
5. How would you investigate which low-FLOP/high-latency bottleneck is responsible?
6. How would profiling distinguish memory bandwidth, transfers, synchronization, poor kernels, layout conversion, fusion problems, dynamic shapes, etc.?
7. Why can fewer FLOPs result in higher latency?
8. Two implementations perform the same operation. One has fewer FLOPs but is slower on GPU. How can that happen?
9. What is the difference between latency and throughput, and why can optimizing one hurt the other?
10. Why does increasing batch size improve GPU throughput?
11. Why does that throughput improvement eventually plateau?
12. Why can a model with fewer parameters use more inference memory than a model with more parameters?
13. What is the computational cost of your model?
14. Could this model run on-device?
15. How would you make the model 4× faster?
16. How would you deploy it on constrained hardware?

## ONNX / deployment / debugging

1. A model is accurate in PyTorch but differs after ONNX export on the target runtime. How would you determine whether the problem is export, unsupported operators, precision, preprocessing, or runtime behavior?
2. PyTorch and ONNX Runtime agree on your workstation, but the embedded target diverges. What do you investigate next?
3. Which metrics would you use to decide whether intermediate activations differ substantially?
4. What is an ONNX graph?
5. What tools are used to debug an ONNX graph?

## Attention / inference frameworks

1. What is TensorRT?
2. Explain FlashAttention.
3. What are Transformers?
4. Why is FlashAttention faster even though exact attention is still O(N^2)?

## Python / concurrency / image decoding
1. What is the GIL in Python?
2. How do you execute code concurrently in Python?
3. For image decompression before GPU processing, should you use threads or processes?
4. What would threaded image decompression and GPU transfer look like in code?
5. How would image decompression be implemented using multiprocessing?
6. What are the pros and cons of multiprocessing versus threads for image decompression?
