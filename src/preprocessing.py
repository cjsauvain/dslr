import numpy as np
import pandas as pd

from src.ft_stats import ft_percentile

_COLUMNS_DROPPED = [
    "Index",
    "Arithmancy",
    "Care of Magical Creatures",
    "Defense Against the Dark Arts",
]


def test_dataset_preprocessing(dataset_path: str, medians: dict) -> pd.DataFrame:
    dataset_df = pd.read_csv(dataset_path).set_index("Index")
    dataset_df = dataset_df.select_dtypes("number")
    to_drop = [col for col in _COLUMNS_DROPPED if col in dataset_df.columns]
    dataset_df = dataset_df.drop(columns=to_drop)

    for course in dataset_df.columns.drop("Hogwarts House"):
        dataset_df[course] = dataset_df[course].fillna(medians[course])

    return dataset_df


def dataset_preprocessing(
    dataset_path: str, validation_ratio: float
) -> tuple[pd.DataFrame, pd.DataFrame | None, dict]:
    dataset_df = pd.read_csv(dataset_path)

    split_index = int(len(dataset_df) * (1 - validation_ratio))

    tmp_dataset_df = dataset_df.select_dtypes("number").drop(columns=_COLUMNS_DROPPED)
    tmp_dataset_df["Hogwarts House"] = dataset_df["Hogwarts House"]
    tmp_dataset_df = tmp_dataset_df.sample(frac=1, random_state=42).reset_index(
        drop=True
    )

    train_df = tmp_dataset_df[:split_index].copy()
    medians = {}
    for course in train_df.columns.drop("Hogwarts House"):
        median = ft_percentile(train_df[course], 50)
        train_df[course] = train_df[course].fillna(median)
        medians[course] = median

    if validation_ratio > 0:
        validation_df = tmp_dataset_df[split_index:].copy()
        for course in validation_df.columns.drop("Hogwarts House"):
            validation_df[course] = validation_df[course].fillna(medians[course])
        return train_df, validation_df, medians

    return train_df, None, medians


def _standardize_data(X: np.ndarray, means: np.ndarray, stds: np.ndarray) -> np.ndarray:
    return (X - means) / stds


def get_features(
    dataset_df: pd.DataFrame,
    means: np.ndarray | None = None,
    stds: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X = np.array(dataset_df.drop(columns="Hogwarts House"))
    out_means: np.ndarray = means if means is not None else X.mean(axis=0)
    out_stds: np.ndarray = stds if stds is not None else X.std(axis=0)
    X = _standardize_data(X, means=out_means, stds=out_stds)
    X = np.hstack((X, np.ones((X.shape[0], 1))))

    return X, out_means, out_stds


def get_target(dataset_df: pd.DataFrame, house: str) -> np.ndarray:
    Y = (dataset_df["Hogwarts House"] == house).astype(int).to_numpy().reshape(-1, 1)

    return Y
