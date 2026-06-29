import math
import pandas as pd


def ft_count(grades_df: pd.Series) -> int:
    nb_entries = len(grades_df)

    for v in grades_df.values:
        if math.isnan(v):
            nb_entries -= 1

    return nb_entries


def ft_mean(grades_df: pd.Series) -> float:
    nb_entries = ft_count(grades_df)
    total = 0
    for v in grades_df.values:
        if not math.isnan(v):
            total += v
    mean = total / (nb_entries)

    return mean


def ft_std(grades_df: pd.Series) -> float:
    mean_df = ft_mean(grades_df)
    variance = 0
    nb_entries = ft_count(grades_df)

    for v in grades_df.values:
        if not math.isnan(v):
            variance += (v - mean_df) ** 2

    std = math.sqrt(variance / (nb_entries - 1))

    return std


def ft_min(grades_df: pd.Series) -> float:
    min_val = float('inf')

    for v in grades_df.values:
        if math.isnan(v):
            continue
        if v < min_val:
            min_val = v

    return min_val


def ft_max(grades_df: pd.Series) -> float:
    max_val = float('-inf')

    for v in grades_df.values:
        if math.isnan(v):
            continue
        if v > max_val:
            max_val = v

    return max_val


def ft_percentile(grades_df: pd.Series, percentile: int) -> float:
    sorted_grades = sorted(
        [v for v in grades_df.values if not math.isnan(v)]
    )
    index = (percentile / 100) * (len(sorted_grades) - 1)
    if index == (int(index)):
        percentile_value = sorted_grades[int(index)]
    else:
        lower_index = int(index)
        upper_index = lower_index + 1
        low = sorted_grades[lower_index]
        high = sorted_grades[upper_index]
        percentile_value = low + (index - lower_index) * (high - low)

    return percentile_value
