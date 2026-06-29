import pandas as pd

from src.parsing import parse_command_line
from visualization import display_histograms


def histogram():
    try:
        args = parse_command_line()
        dataset_df = pd.read_csv(args.dataset)
        display_histograms(dataset_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    histogram()
