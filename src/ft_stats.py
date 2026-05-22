import math
import pandas as pd


def ft_count(df: pd.DataFrame) -> int:
    grades_df = df.select_dtypes(include="number").drop(columns="Index")
    nb_entries = grades_df.shape[0] * grades_df.shape[1]

    for column in grades_df.columns:
        for v in grades_df[column]:
            if math.isnan(v):
                nb_entries -= 1

    return nb_entries

def ft_mean(df: pd.DataFrame) -> float:
    grades_df = df.select_dtypes(include="number").drop(columns="Index")
    nb_entries = grades_df.shape[0] * grades_df.shape[1]
    total = 0
    for column in grades_df.columns:
        for v in grades_df[column]:
            if math.isnan(v):
                nb_entries -= 1
            else:
                total += v
    mean = total / (nb_entries)

    return mean


def ft_std(df: pd.DataFrame) -> float:
    mean_df = ft_mean(df)
    variance = 0
    grades_df = df.select_dtypes(include="number").drop(columns="Index")
    nb_entries = grades_df.shape[0] * grades_df.shape[1]

    for column in grades_df.columns:
        for v in grades_df[column]:
            if not math.isnan(v):
                variance += (v - mean_df) ** 2
            else:
                nb_entries -= 1
    
    std = math.sqrt(variance / (nb_entries - 1))

    return std


def ft_min(df: pd.DataFrame) -> float:
    grades_df = df.select_dtypes(include="number").drop(columns="Index")
    min_val = float('inf')

    for column in grades_df.columns:
        for v in grades_df[column]:
            if v < min_val:
                min_val = v
    
    return min_val


def ft_max(df: pd.DataFrame) -> float:
    grades_df = df.select_dtypes(include="number").drop(columns="Index")
    max_val = float('-inf')

    for column in grades_df.columns:
        for v in grades_df[column]:
            if v > max_val:
                max_val = v
    
    return max_val


def ft_percentile(df: pd.DataFrame, percentile: int) -> float:
    grades_df = df.select_dtypes(include="number").drop(columns="Index")
    sorted_grades_df = sorted([v for v in grades_df.values.flatten() if not math.isnan(v)])
    index = (percentile / 100) * (len(sorted_grades_df) - 1)
    if index == (int(index)):
        percentile_value = sorted_grades_df[int(index)]
    else:
        lower = int(index)
        upper = lower + 1
        percentile_value = sorted_grades_df[lower] + (index - lower) * (sorted_grades_df[upper] - sorted_grades_df[lower])
    
    return percentile_value