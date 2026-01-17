import numpy as np
from sklearn.metrics import confusion_matrix

def iou(mask1, mask2):
    inter = np.logical_and(mask1, mask2).sum()
    union = np.logical_or(mask1, mask2).sum()
    return inter / union if union > 0 else 0

def compute_confusion_matrix(results):
    y_true, y_pred = [], []

    for r in results:
        y_true.extend(r["main_mask"].astype(bool).flatten())
        y_pred.extend(r["generated_mask"].astype(bool).flatten())

    return confusion_matrix(y_true, y_pred)
