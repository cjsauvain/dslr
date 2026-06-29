import pandas as pd

from src.display import display_informations, stats_verification
from src.parsing import parse_command_line


def describe():
    try:
        verify_flag = {
            "name": "--verify",
            "help": "enable verification with pandas describe method",
            "action": "store_true",
            "default": False
        }
        args = parse_command_line(verify_flag)
        dataset_df = pd.read_csv(args.dataset)
        grades_df = (
            dataset_df
            .select_dtypes(include="number")
            .drop(columns="Index")
        )

        display_informations(grades_df)
        if args.verify:
            stats_verification(grades_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    describe()
