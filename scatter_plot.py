import pandas as pd

from visualization import display_scatter_plots
from src.parsing import parse_command_line


def scatter_plot():
    try:
        args = parse_command_line()
        dataset_df = pd.read_csv(args.dataset)
        display_scatter_plots(dataset_df, nb_correlations=6)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    scatter_plot()
