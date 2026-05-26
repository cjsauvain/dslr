import math
import pandas as pd


def ft_count(grades_df: pd.Series) -> int:
    nb_entries = len(grades_df)

    for v in grades_df.values:
        if math.isnan(v):
            nb_entries -= 1

    return nb_entries

def ft_mean(grades_df: pd.Series) -> float:
    nb_entries = len(grades_df)
    total = 0
    for v in grades_df.values:
        if math.isnan(v):
            nb_entries -= 1
        else:
            total += v
    mean = total / (nb_entries)

    return mean


def ft_std(grades_df: pd.Series) -> float:
    mean_df = ft_mean(grades_df)
    variance = 0
    nb_entries = len(grades_df)

    for v in grades_df.values:
        if not math.isnan(v):
            variance += (v - mean_df) ** 2
        else:
            nb_entries -= 1
    
    std = math.sqrt(variance / (nb_entries - 1))

    return std


def ft_min(grades_df: pd.Series) -> float:
    min_val = float('inf')

    for v in grades_df.values:
        if v < min_val:
            min_val = v
    
    return min_val


def ft_max(grades_df: pd.Series) -> float:
    max_val = float('-inf')

    for v in grades_df.values:
        if v > max_val:
            max_val = v
    
    return max_val


def ft_percentile(grades_df: pd.Series, percentile: int) -> float:
    sorted_grades_df = sorted([v for v in grades_df.values if not math.isnan(v)])
    index = (percentile / 100) * (len(sorted_grades_df) - 1)
    if index == (int(index)):
        percentile_value = sorted_grades_df[int(index)]
    else:
        lower = int(index)
        upper = lower + 1
        percentile_value = sorted_grades_df[lower] + (index - lower) * (sorted_grades_df[upper] - sorted_grades_df[lower])
    
    return percentile_value