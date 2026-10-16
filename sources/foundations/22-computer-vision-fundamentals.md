# Computer Vision Fundamentals

## Image Representation and Color Space Grounding
Images are arrays with specific channel order (RGB vs. BGR), bit depth, and color space, and different libraries default differently (OpenCV loads BGR by default, PIL/matplotlib expect RGB), verify actual channel order after loading, since a silent RGB/BGR swap produces plausible-looking but wrong colors without an explicit error.
```python
import cv2
import numpy as np

img_bgr = cv2.imread("photo.jpg")                 # OpenCV: BGR order
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # convert before using with RGB-expecting libraries
print(img_bgr.shape, img_bgr.dtype)                # verify (H, W, 3), uint8
```
Confirm bit depth (`uint8` 0-255 vs. float 0-1 vs. 16-bit) matches what a downstream model/library expects, since silent implicit casting can clip or rescale values incorrectly.
**Pitfalls:** feeding a BGR image directly into a model/visualization expecting RGB, causing subtly wrong-colored (but not obviously broken) results; mixing `uint8` and normalized `float32` images without explicit rescaling, causing values to clip or wrap.

## Image Augmentation and Label-Consistent Transforms
Data augmentation (flips, rotations, color jitter, crops) improves generalization, but geometric transforms must update any associated labels (bounding boxes, keypoints, segmentation masks) consistently, verify a chosen augmentation library actually transforms labels, not just pixels, before assuming correctness.
```python
import albumentations as A

transform = A.Compose(
    [A.HorizontalFlip(p=0.5), A.RandomBrightnessContrast(p=0.3)],
    bbox_params=A.BboxParams(format="pascal_voc", label_fields=["class_labels"]),
)
result = transform(image=img, bboxes=bboxes, class_labels=labels)
```
Visually verify a sample of augmented images with their transformed bounding boxes/masks overlaid, since a subtle coordinate-convention mismatch (normalized vs. pixel, xyxy vs. xywh) silently misaligns labels without throwing an error.
**Pitfalls:** applying a geometric augmentation to images without correspondingly transforming bounding box/mask labels, silently corrupting supervision; mixing up bounding box formats (`xyxy` vs `xywh`, normalized vs. absolute pixels) between augmentation library and model expectations.

## Convolutional Receptive Fields and Feature Map Reasoning
A CNN layer's receptive field (the input region influencing one output activation) grows with depth, stride, and kernel size; verify a claimed receptive field / feature map spatial resolution empirically by inspecting actual tensor shapes at each layer, not just calculating theoretically, since padding/stride implementation choices affect the exact result.
```python
import torch, torch.nn as nn

model = nn.Sequential(nn.Conv2d(3, 16, 3, stride=2, padding=1), nn.Conv2d(16, 32, 3, stride=2, padding=1))
x = torch.randn(1, 3, 224, 224)
for layer in model:
    x = layer(x)
    print(layer, x.shape)   # verify actual spatial downsampling matches expectation
```
Confirm whether a detection/segmentation architecture's output stride actually matches what post-processing code assumes (e.g., mapping feature map cells back to original image coordinates), a common silent bug in custom object detectors.
**Pitfalls:** assuming a theoretical receptive-field formula matches the actual implemented layer behavior without checking real tensor shapes; hardcoding an output stride for coordinate mapping that becomes wrong after modifying the backbone architecture.

## Evaluation Metrics: IoU, mAP, and Confusion Matrices
Object detection/segmentation quality is measured with Intersection-over-Union (IoU) thresholds and mean Average Precision (mAP) at those thresholds, verify which IoU threshold(s) and averaging convention (COCO-style mAP@[.5:.95] vs. Pascal VOC mAP@0.5) a reported number uses before comparing results across papers/tools, since these are not directly comparable.
```python
def iou(box_a, box_b):
    xa, ya = max(box_a[0], box_b[0]), max(box_a[1], box_b[1])
    xb, yb = min(box_a[2], box_b[2]), min(box_a[3], box_b[3])
    inter = max(0, xb - xa) * max(0, yb - ya)
    area_a = (box_a[2]-box_a[0]) * (box_a[3]-box_a[1])
    area_b = (box_b[2]-box_b[0]) * (box_b[3]-box_b[1])
    return inter / (area_a + area_b - inter + 1e-9)
```
Confirm the exact evaluation protocol (dataset split, IoU thresholds, per-class vs. overall averaging) matches between your evaluation harness and any external benchmark number being compared against.
**Pitfalls:** comparing a custom mAP@0.5 implementation directly against a published COCO mAP@[.5:.95] number as if they measure the same thing; computing IoU with an inconsistent box coordinate convention, producing silently wrong overlap values.

# Data Science with NumPy & Pandas

## NumPy Array Views, Copies, and Broadcasting
Slicing a NumPy array returns a view (sharing memory with the original) in most cases, while fancy indexing returns a copy, verify with `.base`/`np.shares_memory()` whether an operation mutates the original array unexpectedly. Broadcasting rules implicitly expand shapes without copying, which can silently apply an operation across an unintended axis if shapes are ambiguous.
```python
import numpy as np

arr = np.arange(10)
view = arr[2:5]
view[0] = 999           # mutates the original array too, since it's a view
print(arr)               # [0, 1, 999, 3, ...]
print(np.shares_memory(arr, view))  # True
```
Verify broadcasting results with an explicit `.shape` check at each step in a multi-array operation, since a shape-compatible but unintended broadcast (e.g., `(3,)` broadcasting against `(3, 1)` instead of the intended `(1, 3)`) produces valid-but-wrong results silently.
**Pitfalls:** mutating a slice expecting it to be an independent copy, unexpectedly corrupting the original array; relying on ambiguous broadcasting shapes that "work" numerically but apply the operation along the wrong axis.

## Pandas Indexing: loc, iloc, and Chained Assignment
`.loc` indexes by label, `.iloc` by integer position, mixing them up on a DataFrame with a non-default integer index produces confusingly different results. Chained indexing (`df[df.x > 0]['y'] = 1`) can silently operate on a temporary copy rather than the original DataFrame, producing a `SettingWithCopyWarning` that should never be ignored.
```python
df.loc[df["status"] == "active", "priority"] = "high"   # correct: single indexing operation
# df[df["status"] == "active"]["priority"] = "high"     # WRONG: chained assignment, may silently no-op
```
Verify any `SettingWithCopyWarning` in logs is actually resolved (not suppressed) by rewriting the operation as a single `.loc` assignment, and confirm index alignment behavior explicitly when combining Series/DataFrames with different indices.
**Pitfalls:** suppressing `SettingWithCopyWarning` instead of fixing the underlying chained-assignment pattern, risking silently-lost updates; assuming `.iloc[5]` and `.loc[5]` reference the same row on a DataFrame whose index isn't the default RangeIndex.

## GroupBy, Aggregation, and Merge Correctness
`groupby` + aggregation is central to tabular analysis; verify the resulting group keys and aggregation semantics (NaN handling, multiple-column grouping) match intent, and verify merge/join operations don't unexpectedly change row counts due to duplicate keys on either side (a fan-out, mirroring the SQL join cardinality issue).
```python
result = df.groupby(["region", "category"], as_index=False).agg(
    total_sales=("sales", "sum"), order_count=("order_id", "nunique")
)
merged = orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
```
Use `merge(..., validate=...)` to assert expected cardinality explicitly, it raises an error immediately if the actual data violates the assumed one-to-one/many-to-one relationship, catching silent row-count inflation early.
**Pitfalls:** merging on a key that has duplicates on the "one" side of an assumed many-to-one relationship, silently multiplying rows; forgetting `dropna=False` when NaN values in the groupby key should form their own group instead of being silently excluded.

## Memory Efficiency and Dtype Optimization
Pandas defaults (object dtype for strings, int64/float64 for numbers) can use far more memory than necessary; verify actual memory usage with `df.memory_usage(deep=True)` before assuming a DataFrame fits comfortably in RAM, and downcast dtypes or use categoricals for repeated string values.
```python
df.info(memory_usage="deep")
df["category"] = df["category"].astype("category")     # large memory savings for low-cardinality strings
df["count"] = pd.to_numeric(df["count"], downcast="integer")
```
Confirm downcasting doesn't silently truncate valid data ranges (e.g., downcasting to `int8` when values can exceed 127), by checking actual min/max values in the column before choosing a smaller dtype.
**Pitfalls:** downcasting a numeric column to a smaller dtype without checking its actual value range, causing silent overflow/wraparound; leaving high-cardinality-looking-but-actually-repetitive string columns as `object` dtype, wasting significant memory versus `category`.

# Computer Vision Fundamentals

## Object Detection Architectures and Anchor/Anchor-Free Design
Object detection models differ in how they propose candidate regions, two-stage detectors (Faster R-CNN) generate region proposals then classify/refine them, one-stage anchor-based detectors (YOLO variants, SSD) predict directly from predefined anchor boxes, and anchor-free detectors (FCOS, newer YOLO versions) predict boxes without predefined anchor shapes; verify which paradigm a specific model checkpoint uses before tuning anchor-related hyperparameters that may not even apply.
```python
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model.predict("image.jpg", conf=0.25, iou=0.45)
for box in results[0].boxes:
    print(box.cls, box.conf, box.xyxy)
```
Verify confidence and NMS IoU thresholds are tuned against a validation set representative of actual deployment conditions (lighting, object scale, occlusion) rather than left at library defaults tuned for a benchmark dataset with different characteristics.
**Pitfalls:** tuning anchor box sizes/ratios for an anchor-free model where the setting has no effect, wasting effort on the wrong hyperparameters; using default confidence/NMS thresholds tuned for a benchmark dataset without re-validating against the actual deployment domain's object scale and density.

## Image Segmentation: Semantic, Instance, and Panoptic
Semantic segmentation labels every pixel with a class (no distinction between object instances), instance segmentation additionally separates individual object instances of the same class, and panoptic segmentation combines both for a complete scene parse; verify which task a specific dataset/model actually targets before evaluating with a mismatched metric (mIoU for semantic vs. mask AP for instance), since these aren't interchangeable.
```python
import torch
from torchvision.models.segmentation import deeplabv3_resnet50

model = deeplabv3_resnet50(weights="DEFAULT").eval()
with torch.no_grad():
    output = model(input_tensor)["out"]
predicted_mask = output.argmax(dim=1)
```
Verify mask post-processing (resizing predictions back to original image resolution, handling class index offsets) matches the exact preprocessing pipeline the model was trained with, since a mismatched resize interpolation method can silently blur or misalign segmentation boundaries.
**Pitfalls:** evaluating an instance segmentation model with a semantic segmentation metric (mIoU) that doesn't account for instance separation, producing a misleading quality signal; using a different image resize/interpolation method at inference than was used during training preprocessing, degrading boundary accuracy without an obvious error.

## Transfer Learning and Fine-Tuning Pretrained Vision Models
Transfer learning reuses a model pretrained on a large dataset (ImageNet, or a vision-language foundation model) as a starting point for a smaller target task, dramatically reducing data and compute requirements versus training from scratch; verify actual layer-freezing strategy (freeze early layers, fine-tune later layers/head only, or full fine-tuning) matches the target dataset's size and similarity to the pretraining domain, full fine-tuning on a very small target dataset risks catastrophic forgetting and overfitting.
```python
model = torchvision.models.resnet50(weights="IMAGENET1K_V2")
for param in model.parameters():
    param.requires_grad = False   # freeze pretrained backbone
model.fc = torch.nn.Linear(model.fc.in_features, num_target_classes)  # replace and train only the head
```
Verify normalization statistics (mean/std per channel) used at inference exactly match those the pretrained backbone was originally trained with, since a mismatch silently shifts the input distribution the backbone expects, degrading transfer performance without an explicit error.
**Pitfalls:** fully fine-tuning a large pretrained model on a very small target dataset, causing catastrophic forgetting of useful pretrained features and overfitting to the small dataset; using the target dataset's own normalization statistics instead of the pretrained model's original training statistics, silently degrading feature quality.

## Video Understanding and Temporal Consistency
Video models must handle the temporal dimension in addition to spatial content, through 3D convolutions, frame-sampling strategies, or temporal attention, and verify frame sampling rate/stride actually captures the motion granularity needed for the task (action recognition needs different sampling than scene classification), since undersampling can miss brief but critical motion cues.
```python
import decord
vr = decord.VideoReader("clip.mp4")
frame_indices = list(range(0, len(vr), max(1, len(vr) // 16)))  # uniformly sample 16 frames
frames = vr.get_batch(frame_indices).asnumpy()
```
Verify temporal consistency of per-frame predictions (a per-frame object detector applied naively to video can produce flickering, inconsistent boxes across adjacent frames) and consider explicit tracking/smoothing if frame-to-frame consistency matters for the application.
**Pitfalls:** sampling too few or unevenly spaced frames for an action-recognition task, missing the specific motion pattern that distinguishes similar-looking actions; applying a single-image model frame-by-frame to video without any temporal smoothing, producing visibly flickering or inconsistent predictions across frames.

# Data Science with NumPy & Pandas

## Vectorization versus Explicit Loops
NumPy and Pandas operations implemented in C under the hood (vectorized operations) are dramatically faster than equivalent Python-level loops due to avoiding per-element interpreter overhead; verify a suspected performance bottleneck is actually a non-vectorized loop with a profiler before assuming an operation is "just slow," and confirm a proposed vectorized replacement produces numerically identical results, not just a superficially similar-looking one.
```python
import numpy as np
import time

data = np.random.rand(1_000_000)
start = time.perf_counter()
result_loop = [x ** 2 + 1 for x in data]              # slow: Python-level loop
print("loop:", time.perf_counter() - start)

start = time.perf_counter()
result_vectorized = data ** 2 + 1                       # fast: vectorized C implementation
print("vectorized:", time.perf_counter() - start)
```
Verify vectorized replacements handle edge cases (NaN propagation, empty arrays, mixed dtypes) identically to the original loop-based logic before fully replacing it, since vectorized NumPy operations can have subtly different behavior around these edge cases.
**Pitfalls:** using `df.apply()` with a Python function row-by-row when a vectorized NumPy/Pandas expression would be an order of magnitude faster; assuming a vectorized rewrite is behaviorally identical without testing edge cases like NaN or empty-input handling explicitly.

## Time Series Handling with Pandas DatetimeIndex
Pandas provides rich time-series functionality (resampling, rolling windows, timezone handling) built around `DatetimeIndex`; verify timezone-awareness explicitly, mixing timezone-naive and timezone-aware timestamps raises errors or silently produces wrong results depending on the operation, and daylight-saving-time transitions can create ambiguous or nonexistent local times that need explicit handling.
```python
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
df = df.set_index("timestamp")
daily = df.resample("D").agg({"revenue": "sum", "orders": "count"})
rolling_avg = df["revenue"].rolling("7D").mean()
```
Verify resampling aggregation choices (sum vs. mean vs. last) match the actual semantics of each column, summing a "current balance" column across a resample period would be nonsensical, while summing a "transactions" column is correct.
**Pitfalls:** mixing timezone-naive and timezone-aware timestamps in the same DataFrame, causing comparison/join errors or silent UTC-offset misalignment; resampling a non-additive column (like a snapshot balance) with `sum()` instead of `last()`/`mean()`, producing meaningless aggregated values.

## Multi-Index and Hierarchical Data Reshaping
Pandas MultiIndex enables hierarchical row/column labeling for higher-dimensional tabular data, and `pivot`/`pivot_table`/`melt`/`stack`/`unstack` reshape between long and wide formats; verify the reshape operation actually preserves the expected row count and no unintended aggregation occurs (`pivot_table`'s default aggregation function silently averages duplicate index/column combinations unless a different function is specified).
```python
wide = df.pivot_table(index="date", columns="region", values="revenue", aggfunc="sum")
long_again = wide.reset_index().melt(id_vars="date", var_name="region", value_name="revenue")
```
Verify `pivot` (which raises an error on duplicate index/column combinations) versus `pivot_table` (which silently aggregates them) matches the actual data's uniqueness guarantees, choosing `pivot` deliberately when duplicates should be treated as a data-quality error rather than silently averaged away.
**Pitfalls:** using `pivot_table`'s default mean aggregation when duplicates actually represent a data-quality bug that should raise an error instead of being silently averaged; losing track of which level of a MultiIndex a subsequent operation applies to, producing results aggregated over the wrong dimension.

## Data Validation and Schema Enforcement in Pipelines
Production data pipelines benefit from explicit schema validation (column types, value ranges, nullability, uniqueness constraints) at ingestion boundaries using libraries like `pandera` or `great_expectations`, catching upstream data quality regressions immediately rather than allowing them to silently propagate into downstream analysis or model training.
```python
import pandera as pa

schema = pa.DataFrameSchema({
    "order_id": pa.Column(int, unique=True),
    "total": pa.Column(float, checks=pa.Check.ge(0)),
    "status": pa.Column(str, checks=pa.Check.isin(["pending", "shipped", "cancelled"])),
})
validated_df = schema.validate(df)   # raises SchemaError with details on first violation
```
Verify validation failures are surfaced loudly (pipeline halts, alert fires) rather than logged and silently skipped, since a schema violation usually indicates an upstream data source changed in a way that could corrupt all downstream results.
**Pitfalls:** validating schema once during initial development and never re-running it as part of the ongoing production pipeline, missing when an upstream data source silently changes format; catching schema validation errors and logging them without halting the pipeline, allowing corrupted data to flow downstream anyway.
