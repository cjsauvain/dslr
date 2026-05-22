import pandas as pd
import sys

def parse_command_line() -> pd.DataFrame:
    args = sys.argv

    if len(args) != 2:
        print("Usage: python describe.py <dataset_path>", file=sys.stderr)
        sys.exit(1)
    
    dataset_df = pd.read_csv(args[1])

    return dataset_df
