import pandas as pd
# from .ft_stats import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile


def _display_header(grades_df: pd.DataFrame):
    print("\n-------------------------------------------------------------------------")
    print("\nHOGWARTS STUDENTS' GRADES STATISTICS\n")
    print(f"{grades_df.columns}")


# def _display_count(dataset_df: pd.DataFrame):
#     count_gryffindor = ft_count(gryffindor_df)

#     print(f"Count\t\t{count_gryffindor}\t\t{count_hufflepuff}\t\t{count_ravenclaw}\t\t{count_slytherin}")


# def _display_mean(dataset_df: pd.DataFrame):
#     mean_gryffindor = ft_mean(gryffindor_df)
#     mean_hufflepuff = ft_mean(hufflepuff_df)
#     mean_ravenclaw = ft_mean(ravenclaw_df)
#     mean_slytherin = ft_mean(slytherin_df)

#     print(f"Mean\t\t{mean_gryffindor:.2f}\t\t{mean_hufflepuff:.2f}\t\t{mean_ravenclaw:.2f}\t\t{mean_slytherin:.2f}")


# def _display_std(dataset_df: pd.DataFrame):
#     std_gryffindor = ft_std(gryffindor_df)
#     std_hufflepuff = ft_std(hufflepuff_df)
#     std_ravenclaw = ft_std(ravenclaw_df)
#     std_slytherin = ft_std(slytherin_df)

#     print(f"Std\t\t{std_gryffindor:.2f}\t{std_hufflepuff:.2f}\t{std_ravenclaw:.2f}\t{std_slytherin:.2f}")


# def _display_min(dataset_df: pd.DataFrame):
#     min_gryffindor = ft_min(gryffindor_df)
#     min_hufflepuff = ft_min(hufflepuff_df)
#     min_ravenclaw = ft_min(ravenclaw_df)
#     min_slytherin = ft_min(slytherin_df)

#     print(f"min\t\t{min_gryffindor:.2f}\t{min_hufflepuff:.2f}\t{min_ravenclaw:.2f}\t{min_slytherin:.2f}")


# def _display_max(dataset_df: pd.DataFrame):
#     max_gryffindor = ft_max(gryffindor_df)
#     max_hufflepuff = ft_max(hufflepuff_df)
#     max_ravenclaw = ft_max(ravenclaw_df)
#     max_slytherin = ft_max(slytherin_df)

#     print(f"max\t\t{max_gryffindor:.2f}\t{max_hufflepuff:.2f}\t{max_ravenclaw:.2f}\t{max_slytherin:.2f}")


# def _display_percentile(dataset_df: pd.DataFrame):
#     percentile_gryffindor = ft_percentile(gryffindor_df, percentile)
#     percentile_hufflepuff = ft_percentile(hufflepuff_df, percentile)
#     percentile_ravenclaw = ft_percentile(ravenclaw_df, percentile)
#     percentile_slytherin = ft_percentile(slytherin_df, percentile)

#     print(f"{percentile}%\t\t{percentile_gryffindor:.2f}\t\t{percentile_hufflepuff:.2f}\t\t{percentile_ravenclaw:.2f}\t\t{percentile_slytherin:.2f}")


# def stats_verification(dataset_df: pd.DataFrame):
#     print("\n-------------------------------------------------------------------------")
#     print("\nVALIDATION WITH PANDAS\n")
#     print(
#         dataset_df.groupby("Hogwarts House").apply(
#             lambda x: x.select_dtypes(include="number")
#                 .drop(columns="Index")
#                 .stack()
#                 .describe()
#             ).T
#     )
#     print("\n-------------------------------------------------------------------------")


def display_informations(grades_df: pd.DataFrame):
    _display_header(grades_df)
    # _display_count(dataset_df)
    # _display_mean(dataset_df)
    # _display_std(dataset_df)
    # _display_min(dataset_df)
    # _display_percentile(dataset_df)
    # _display_percentile(dataset_df)
    # _display_percentile(dataset_df)
    # _display_max(dataset_df)
