from src.display import display_informations, stats_verification
from src.parsing import parse_command_line


def describe():
    try:
        dataset_df = parse_command_line()
        display_informations(dataset_df.select_dtypes(include="number").drop(columns="Index"))
        stats_verification(dataset_df.select_dtypes(include="number").drop(columns="Index"))
    
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    describe()