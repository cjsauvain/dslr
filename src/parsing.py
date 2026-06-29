import argparse


def ratio_between_0_and_1(value: str) -> float:
    f = float(value)

    if not 0 <= f < 1:
        raise argparse.ArgumentTypeError(
            f"validation ratio must be in the range [0, 1[, got {f}"
        )

    return f


def training_parsing() -> argparse.Namespace:
    learning_curve_option = {
        "name": "--learning-curve",
        "help": "plot the training (+ validation) loss over iterations",
        "action": "store_true",
        "default": False
    }
    validation_ratio_option = {
        "name": "--validation-ratio",
        "help": "validation ratio used to split the training dataset",
        "type": ratio_between_0_and_1,
        "default": 0
    }
    confusion_matrix_option = {
        "name": "--confusion-matrix",
        "help": "display confusion matrix if validation is enabled",
        "action": "store_true",
        "default": False
    }
    metrics_option = {
        "name": "--metrics",
        "help": "display metrics if validation is enabled",
        "action": "store_true",
        "default": False
    }

    args = parse_command_line(
        learning_curve_option,
        validation_ratio_option,
        confusion_matrix_option,
        metrics_option
    )

    return args


def parse_command_line(*options: dict) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("dataset", help="Training dataset path")

    for option in options:
        name = option["name"]
        kwargs = {k: v for k, v in option.items() if k != "name"}
        parser.add_argument(name, **kwargs)

    return parser.parse_args()
