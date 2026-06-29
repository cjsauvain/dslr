import pandas as pd
import numpy as np

from src.preprocessing import get_features, get_target
from src.metrics import _HOUSES


_LOG_CLIP = 1e-15
_CONVERGENCE_LIMIT = 1e-9
_MAX_ITER = 10000
_LEARNING_RATE = 0.01


def prediction(
        dataset_df: pd.DataFrame,
        weights: dict,
        means: np.ndarray,
        stds: np.ndarray
) -> pd.Series:
    houses = list(weights.keys())
    X, _, _ = get_features(dataset_df, means=means, stds=stds)

    Y = pd.DataFrame(index=dataset_df.index)
    for house in houses:
        house_thetas = np.array(weights[house]).reshape(-1, 1)
        Y[house] = _model(X, house_thetas).flatten()

    Y["Selected House"] = Y.idxmax(axis=1)

    return Y["Selected House"]


def _model(X: np.ndarray, thetas: np.ndarray) -> np.ndarray:
    Z = X.dot(thetas)

    return (1 / (1 + np.exp(-Z)))


def _cost_function(X: np.ndarray, Y: np.ndarray, thetas: np.ndarray) -> float:
    m = len(Y)
    model_res = _model(X, thetas)
    model_res = np.clip(model_res, _LOG_CLIP, 1 - _LOG_CLIP)
    y_is_one = Y * np.log(model_res)
    y_is_zero = (1 - Y) * np.log(1 - model_res)

    return -(1/m) * np.sum(y_is_one + y_is_zero)


def _gradient(X: np.ndarray, Y: np.ndarray, thetas: np.ndarray) -> np.ndarray:
    m = len(Y)

    return (1/m) * X.T.dot(_model(X, thetas) - Y)


def _train_house_model(
        X: np.ndarray,
        X_validation: np.ndarray | None,
        Y: np.ndarray,
        Y_validation: np.ndarray | None,
        learning_curve_opt: bool
) -> tuple[np.ndarray, dict]:
    thetas = np.zeros((X.shape[1], 1))
    iter = 0
    cost = _cost_function(X, Y, thetas)
    old_cost = float('inf')

    cost_history = {
        "training": [],
        "validation": []
    }
    while abs(old_cost - cost) > _CONVERGENCE_LIMIT and iter < _MAX_ITER:
        old_cost = cost

        grad = _gradient(X, Y, thetas)
        thetas = thetas - _LEARNING_RATE * grad
        cost = _cost_function(X, Y, thetas)
        if learning_curve_opt:
            cost_history["training"].append(cost)
            if X_validation is not None and Y_validation is not None:
                validation_cost = _cost_function(
                    X_validation,
                    Y_validation,
                    thetas
                )
                cost_history["validation"].append(validation_cost)

        iter += 1

    return thetas, cost_history


def _build_json_content_skeleton(means: list, stds: list) -> dict:
    json_content = {
        "normalization": {
            "means": means,
            "stds": stds
        },
        "weights": {},
        "medians": []
    }

    return json_content


def logreg(
        dataset_df: pd.DataFrame,
        validation_df: pd.DataFrame | None,
        medians: dict,
        learning_curve_opt: bool
) -> tuple[dict, np.ndarray, np.ndarray, dict | None]:
    X, means, stds = get_features(dataset_df)
    X_validation, _, _ = get_features(validation_df, means=means, stds=stds) \
        if validation_df is not None else (None, None, None)

    json_content = _build_json_content_skeleton(means.tolist(), stds.tolist())

    houses_cost_histories: dict[str, dict] = {house: {} for house in _HOUSES}
    for index, house in enumerate(dataset_df["Hogwarts House"].unique()):
        Y = get_target(dataset_df, house)
        Y_validation = get_target(validation_df, house) \
            if validation_df is not None else None
        thetas, house_cost_history = _train_house_model(
            X,
            X_validation,
            Y,
            Y_validation,
            learning_curve_opt
        )
        houses_cost_histories[house] = house_cost_history
        json_content["weights"][house] = thetas.flatten().tolist()

    json_content["medians"] = medians

    return json_content, means, stds, houses_cost_histories
