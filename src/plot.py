from matplotlib.axes import Axes
from matplotlib import pyplot as plt
import pandas as pd
from pandas import Series
from numpy import array, triu, fill_diagonal


def build_histogram(
        ax: Axes,
        course_grades: Series,
        course: str,
        house_color: str,
        set_xlabel: bool,
        set_ylabel: bool
):

    ax.hist(course_grades, color=house_color, alpha=0.5)

    ax.set_title(course)
    if set_xlabel == True:
        ax.set_xlabel("grades")
    if set_ylabel == True:
        ax.set_ylabel("# of students")


def display_scatter_plot(grades_df: pd.DataFrame):
    ############################################
    # DROP NA VALUES !!!!!!!!!!!!!!!!!!!!!!!!!!#
    ############################################
    corr_array = array(grades_df.corr().abs())
    fill_diagonal(corr_array, 0)
    corr_array = triu(corr_array)
    corr = pd.DataFrame(corr_array, index=grades_df.columns, columns=grades_df.columns)
    top_four_correlations = corr.stack().nlargest(4)

    figure, axes = plt.subplots(nrows=2, ncols=2)
    figure.suptitle("Most correlated features")
    axes = axes.flatten()

    for index, courses in enumerate(top_four_correlations.index):
        axes[index].scatter(grades_df[courses[0]], grades_df[courses[1]])
        axes[index].set_xlabel(courses[0] + " Grades")
        axes[index].set_ylabel(courses[1] + " Grades")

    plt.tight_layout()
    plt.show()


def display_pair_plot(grades_df: pd.DataFrame):
    pass