import pandas as pd
import numpy as np

from src.logreg import prediction
from src.metrics import build_confusion_matrix
from src.visualization import display_metrics, display_confusion_matrix


def run_validation_and_metrics(
        validation_df: pd.DataFrame,
        weights: dict,
        means: np.ndarray,
        stds: np.ndarray,
        confusion_matrix_opt: bool,
        metrics_opt: bool
):
    if not (confusion_matrix_opt or metrics_opt):
        return

    Y = prediction(validation_df, weights, means, stds)

    confusion_matrix = build_confusion_matrix(
        validation_df["Hogwarts House"],
        Y
    )
    if confusion_matrix_opt:
        display_confusion_matrix(confusion_matrix)
    if metrics_opt:
        display_metrics(confusion_matrix)
