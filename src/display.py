from operator import index

import pandas as pd

from .ft_stats import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile


COL_WIDTH = 20


def _display_header(grades_df: pd.DataFrame, col_width_factor: int):
    print("\n", ' ' * (COL_WIDTH // 2), end="")
    for course in grades_df.columns:
        print(f"{course:<{col_width_factor * COL_WIDTH}}", end="")
    print()


def _display_count(grades_df: pd.DataFrame, col_width_factor: int):
    print(f"{'Count':<{COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(f"{ft_count(grades_df[course]):<{col_width_factor * COL_WIDTH}}", end="")
    print()


def _display_mean(grades_df: pd.DataFrame, col_width_factor: int):
    print(f"{'Mean':<{COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(f"{ft_mean(grades_df[course]):<{col_width_factor * COL_WIDTH}.2f}", end="")
    print()


def _display_std(grades_df: pd.DataFrame, col_width_factor: int):
    print(f"{'Std':<{COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(f"{ft_std(grades_df[course]):<{col_width_factor * COL_WIDTH}.2f}", end="")
    print()


def _display_min(grades_df: pd.DataFrame, col_width_factor: int):
    print(f"{'min':<{COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(f"{ft_min(grades_df[course]):<{col_width_factor * COL_WIDTH}.2f}", end="")
    print()


def _display_max(grades_df: pd.DataFrame, col_width_factor: int):
    print(f"{'max':<{COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(f"{ft_max(grades_df[course]):<{col_width_factor * COL_WIDTH}.2f}", end="")
    print()


def _display_percentile(grades_df: pd.DataFrame, percentile: int, col_width_factor: int):
    label = f"{percentile}%"
    print(f"{label:<{COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(f"{ft_percentile(grades_df[course], percentile):<{col_width_factor * COL_WIDTH}.2f}", end="")
    print()


def stats_verification(grades_df: pd.DataFrame):
    print("\n----------------------------------------------------------------------------------------------------------------------")
    print("\nVALIDATION WITH PANDAS\n")
    print(grades_df.iloc[:, :6].drop(columns="Defense Against the Dark Arts").describe().round(2))
    print(grades_df.iloc[:, 6:].drop(columns="Care of Magical Creatures").describe().round(2))
    print(grades_df[["Defense Against the Dark Arts", "Care of Magical Creatures"]].describe().round(2))
    print("\n----------------------------------------------------------------------------------------------------------------------")


def _display_half(grades_df: pd.DataFrame, col_width_factor=1):
    _display_header(grades_df, col_width_factor)
    _display_count(grades_df, col_width_factor)
    _display_mean(grades_df, col_width_factor)
    _display_std(grades_df, col_width_factor)
    _display_min(grades_df, col_width_factor)
    _display_percentile(grades_df, 25, col_width_factor)
    _display_percentile(grades_df, 50, col_width_factor)
    _display_percentile(grades_df, 75, col_width_factor)
    _display_max(grades_df, col_width_factor)


def display_informations(grades_df: pd.DataFrame):
    print("\n----------------------------------------------------------------------------------------------------------------------")
    print("\nHOGWARTS STUDENTS' GRADES STATISTICS", end="\n")
    _display_half(grades_df.iloc[:, :6].drop(columns="Defense Against the Dark Arts"))
    _display_half(grades_df.iloc[:, 6:].drop(columns="Care of Magical Creatures"))
    _display_half(grades_df[["Defense Against the Dark Arts", "Care of Magical Creatures"]], 2)
