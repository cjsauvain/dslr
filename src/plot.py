from matplotlib.axes import Axes
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame
from numpy import array, triu, fill_diagonal


HOUSE_COLORS = {
    "Gryffindor": "red",
    "Hufflepuff": "yellow",
    "Ravenclaw": "blue",
    "Slytherin": "green"
}


def build_histogram(
        ax: Axes,
        grades_by_houses_df: dict[str, DataFrame],
        course: str,
):
    for house, grades in grades_by_houses_df.items():
        ax.hist(grades[course], color=HOUSE_COLORS[house], alpha=0.5)
        ax.set_title(course)

def display_scatter_plot(grades_df: pd.DataFrame):
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