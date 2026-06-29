import pandas as pd
import json

from src.parsing import parse_command_line
from src.preprocessing import test_dataset_preprocessing
from src.logreg import prediction


def _retrieve_model_json(model_json_path: str) -> dict:
    with open(model_json_path, "r") as file:
        model_json = json.load(file)

    return model_json


def _run_prediction(dataset_df: pd.DataFrame, model_json: dict):
    weights = model_json["weights"]
    means = model_json["normalization"]["means"]
    stds = model_json["normalization"]["stds"]

    Y = prediction(dataset_df, weights, means=means, stds=stds)

    Y.to_csv("houses.csv")


def predict():
    try:
        help = "JSON file with trained weights and preprocessing parameters"
        model_file_argument = {
            "name": "model_json",
            "help": help
        }
        args = parse_command_line(model_file_argument)
        model_json = _retrieve_model_json(args.model_json)
        dataset_df = test_dataset_preprocessing(
            args.dataset,
            model_json["medians"]
        )

        _run_prediction(dataset_df, model_json)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    predict()
