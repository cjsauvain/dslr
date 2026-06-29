import pandas as pd

from .ft_stats import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile


_COL_WIDTH = 20


def _display_header(grades_df: pd.DataFrame, col_width_factor: int):
    print("\n", ' ' * (_COL_WIDTH // 2), end="")
    width = col_width_factor * _COL_WIDTH
    for course in grades_df.columns:
        print(f"{course:<{width}}", end="")
    print()


def _display_stat(
        grades_df: pd.DataFrame,
        col_width_factor: int,
        stat_label: str,
        stat_func,
        fmt=".2f"
):
    print(f"{stat_label:<{_COL_WIDTH // 2}}", end=" ")
    width = col_width_factor * _COL_WIDTH
    for course in grades_df.columns:
        print(
            f"{stat_func(grades_df[course]):<{width}{fmt}}",
            end=""
        )
    print()


def _display_percentile(
        grades_df: pd.DataFrame,
        percentile: int,
        col_width_factor: int
):
    width = col_width_factor * _COL_WIDTH
    label = f"{percentile}%"
    print(f"{label:<{_COL_WIDTH // 2}}", end=" ")
    for course in grades_df.columns:
        print(
            f"{ft_percentile(grades_df[course], percentile):<{width}.2f}",
            end=""
        )
    print()


def _display_half(grades_df: pd.DataFrame, col_width_factor=1):
    _display_header(grades_df, col_width_factor)
    _display_stat(grades_df, col_width_factor, "Count", ft_count, "")
    _display_stat(grades_df, col_width_factor, "Mean", ft_mean)
    _display_stat(grades_df, col_width_factor, "Std", ft_std)
    _display_stat(grades_df, col_width_factor, "min", ft_min)
    _display_percentile(grades_df, 25, col_width_factor)
    _display_percentile(grades_df, 50, col_width_factor)
    _display_percentile(grades_df, 75, col_width_factor)
    _display_stat(grades_df, col_width_factor, "max", ft_max)


def stats_verification(grades_df: pd.DataFrame):
    print("\nVALIDATION WITH PANDAS\n")
    print(
        grades_df
        .iloc[:, :6]
        .drop(columns="Defense Against the Dark Arts")
        .describe()
        .round(2)
    )
    print(
        grades_df
        .iloc[:, 6:]
        .drop(columns="Care of Magical Creatures")
        .describe()
        .round(2)
    )
    print(
        grades_df[[
            "Defense Against the Dark Arts",
            "Care of Magical Creatures"
        ]]
        .describe()
        .round(2)
    )
    print("\n" + "-" * 118)


def display_informations(grades_df: pd.DataFrame):
    print("\n" + "-" * 118)
    print("\nHOGWARTS STUDENTS' GRADES STATISTICS", end="\n")
    _display_half(
        grades_df
        .iloc[:, :6]
        .drop(columns="Defense Against the Dark Arts")
    )
    _display_half(
        grades_df
        .iloc[:, 6:]
        .drop(columns="Care of Magical Creatures")
    )
    _display_half(
        grades_df[[
            "Defense Against the Dark Arts",
            "Care of Magical Creatures"
        ]],
        2,
    )
    print("\n" + "-" * 118)
