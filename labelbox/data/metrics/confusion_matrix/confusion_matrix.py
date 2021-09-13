# type: ignore
from collections import defaultdict
from labelbox.data.annotation_types import feature
from labelbox.data.annotation_types.metrics import ConfusionMatrixMetric
from typing import List, Optional, Union
from ...annotation_types import (Label, ObjectAnnotation,
                                 ClassificationAnnotation)

from ..processing import get_feature_pairs
from .calculation import confusion_matrix
from .calculation import feature_confusion_matrix
import numpy as np


def confusion_matrix_metric(ground_truths: List[Union[
    ObjectAnnotation, ClassificationAnnotation]],
                            predictions: List[Union[ObjectAnnotation,
                                                    ClassificationAnnotation]],
                            include_subclasses=True,
                            iou=0.5) -> List[ConfusionMatrixMetric]:
    """
    Computes miou between two sets of annotations.
    This will most commonly be used for data row level metrics.
    Each class in the annotation list is weighted equally in the iou score.

    Args:
        ground_truth : Label containing human annotations or annotations known to be correct
        prediction: Label representing model predictions
        include_subclasses (bool): Whether or not to include subclasses in the iou calculation.
            If set to True, the iou between two overlapping objects of the same type is 0 if the subclasses are not the same.
    Returns:
        Returns a list of ScalarMetrics. Will be empty if there were no predictions and labels. Otherwise a single metric will be returned.
    """
    if not (0. < iou < 1.):
        raise ValueError("iou must be between 0 and 1")

    value = confusion_matrix(ground_truths, predictions, include_subclasses,
                             iou)
    # If both gt and preds are empty there is no metric
    if value is None:
        return []

    return [
        ConfusionMatrixMetric(
            metric_name=f"confusion_matrix_{int(iou*100)}pct_iou", value=value)
    ]


def feature_confusion_matrix_metric(
    ground_truths: List[Union[ObjectAnnotation, ClassificationAnnotation]],
    predictions: List[Union[ObjectAnnotation, ClassificationAnnotation]],
    include_subclasses=True,
    iou: float = 0.5,
) -> List[ConfusionMatrixMetric]:
    """
    Computes the miou for each type of class in the list of annotations.

    Args:
        ground_truth : Label containing human annotations or annotations known to be correct
        prediction: Label representing model predictions
        include_subclasses (bool): Whether or not to include subclasses in the iou calculation.
            If set to True, the iou between two overlapping objects of the same type is 0 if the subclasses are not the same.
    Returns:
        Returns a list of ScalarMetrics.
        There will be one metric for each class in the union of ground truth and prediction classes.
    """
    # Classifications are supported because we just take a naive approach to them..
    annotation_pairs = get_feature_pairs(predictions, ground_truths)
    metrics = []
    for key in annotation_pairs:
        value = feature_confusion_matrix(annotation_pairs[key][0],
                                         annotation_pairs[key][1],
                                         include_subclasses, iou)
        if value is None:
            continue
        metrics.append(
            ConfusionMatrixMetric(
                metric_name=f"confusion_matrix_{int(iou*100)}pct_iou",
                feature_name=key,
                value=value))
    return metrics
