import pandas as pd
import numpy as np


def multinomial_logreg(
        dataset_df: pd.DataFrame,
        medians: dict,
        validation_option: float,
        learning_curve_option: bool
) -> tuple[dict, np.ndarray, np.ndarray]:
    return {}, np.array((1, 1)), np.array((1, 1))
