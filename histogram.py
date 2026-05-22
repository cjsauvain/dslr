from src.utils import split_dataframe_by_houses
from src.parsing import parse_command_line
from src.plot import display_histograms


def histogram():
    try:
        dataset_df = parse_command_line()
        gryffindor_df, hufflepuff_df, ravenclaw_df, slytherin_df = split_dataframe_by_houses(dataset_df)
        display_histograms(gryffindor_df, hufflepuff_df, ravenclaw_df, slytherin_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    histogram()
