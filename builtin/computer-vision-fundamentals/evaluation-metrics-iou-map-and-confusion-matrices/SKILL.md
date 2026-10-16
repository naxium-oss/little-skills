---
name: evaluation-metrics-iou-map-and-confusion-matrices
description: "Use when \"evaluation metrics iou map and confusion matrices\" is the work."
---

# Evaluation Metrics: IoU, mAP, and Confusion

comparing a custom mAP@0.5.

1. Do not: comparing a custom mAP@0.5 implementation directly against a published COCO mAP@[.5:.95] number as if.
2. Do not: computing IoU with an inconsistent box coordinate convention, producing silently wrong overlap values.

Example:
```bash
confirm channel order, value range, and resolution at each stage
```

Check: Do not: comparing a.
