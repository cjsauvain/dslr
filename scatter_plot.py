from src.plot import display_scatter_plot
from src.parsing import parse_command_line


def scatter_plot():
    try:
        dataset_df = parse_command_line()
        display_scatter_plot(dataset_df)
    
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    scatter_plot()