import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

from src.parsing import parse_command_line
from visualization import display_histograms, display_scatter_plots


def _display_pair_plots(dataset_df: pd.DataFrame):
    with PdfPages("pair_plots.pdf") as pdf:
        display_histograms(dataset_df, pdf=pdf)
        display_scatter_plots(dataset_df, pdf=pdf)


def pair_plot():
    try:
        args = parse_command_line()
        dataset_df = pd.read_csv(args.dataset)
        _display_pair_plots(dataset_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    pair_plot()
