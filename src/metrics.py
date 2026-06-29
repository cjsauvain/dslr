import pandas as pd
import numpy as np


_HOUSES = [
    "Gryffindor",
    "Hufflepuff",
    "Ravenclaw",
    "Slytherin"
]


def build_confusion_matrix(y_true: pd.Series, y_pred: pd.Series) -> np.ndarray:
    nb_houses = len(_HOUSES)
    matrix = np.zeros((nb_houses, nb_houses), dtype=int)

    for student_true, student_predict in zip(y_true, y_pred):
        row_index = _HOUSES.index(student_true)
        column_index = _HOUSES.index(student_predict)

        matrix[row_index][column_index] += 1

    return matrix


def ft_f1_score(precision: float, recall: float) -> float:
    return 2 / (1/precision + 1/recall)


def ft_precision(matrix: np.ndarray, house_index: int) -> float:
    tp = matrix[house_index][house_index]
    fp = matrix[:, house_index].sum() - tp

    return tp / (tp + fp)


def ft_recall(matrix: np.ndarray, house_index: int) -> float:
    tp = matrix[house_index][house_index]
    fn = matrix[house_index].sum() - tp

    return tp / (tp + fn)


def ft_accuracy(matrix: np.ndarray) -> float:
    return np.trace(matrix) / matrix.sum()
