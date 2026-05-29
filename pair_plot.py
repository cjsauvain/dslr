from src.plot import display_pair_plot
from src.parsing import parse_command_line


def pair_plot():
    try:
        dataset_df = parse_command_line()
        grades_df = dataset_df.select_dtypes(include="number").drop(columns="Index")
        display_pair_plot(grades_df)
    
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    pair_plot()