import math
from tkinter import Tk
from numpy import ndarray
from pandas import DataFrame
from src.parsing import parse_command_line
from src.plot import build_histogram
from matplotlib import patches, pyplot as plt
from matplotlib.lines import Line2D


def _get_grades_by_houses(dataset_df: DataFrame) -> dict[str, DataFrame]:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    return {
        house: dataset_df[dataset_df["Hogwarts House"] == house]
            .select_dtypes("number")
            .drop(columns="Index", errors="ignore")
            for house in houses
    }


def _set_figure_and_axes(nb_courses: int, nb_columns: int = 5) -> ndarray:
    nb_rows = math.ceil(nb_courses / nb_columns)

    figure, axes = plt.subplots(nrows=nb_rows, ncols=nb_columns)
    figure.suptitle("Hogwarts Grade Distribution by Course")
    house_colors_handles = [
        patches.Patch(color="red", label="Gryffindor", alpha=0.5),
        patches.Patch(color="yellow", label="Hufflepuff", alpha=0.5),
        patches.Patch(color="blue", label="Ravenclaw", alpha=0.5),
        patches.Patch(color="green", label="Slytherin", alpha=0.5)
    ]
    ax_labels_handles = [
        Line2D([], [], color="none", label="X: Grades"),
        Line2D([], [], color="none", label="Y: # of students"),
    ]
    figure.legend(
        handles=house_colors_handles,
        bbox_to_anchor=(0.94, 0.21),
        fontsize=18
    )
    figure.legend(
        handles=ax_labels_handles,
        handlelength=0,
        handletextpad=0,
        bbox_to_anchor=(0.81, 0.135),
        fontsize=18
    )
    axes = axes.flatten()

    screen_resolution = Tk()
    dpi = figure.get_dpi()
    screen_width = screen_resolution.winfo_screenwidth()
    screen_height = screen_resolution.winfo_screenheight()
    figure.set_figwidth((screen_width * 0.95) / dpi)
    figure.set_figheight((screen_height * 0.90) / dpi)
    screen_resolution.destroy()

    return axes


def _loop_over_courses(dataset_df: DataFrame):
    grades_df = dataset_df.select_dtypes("number").drop(columns="Index", errors="ignore")
    grades_by_houses_df = _get_grades_by_houses(dataset_df)

    nb_courses = len(grades_df.columns)
    axes = _set_figure_and_axes(nb_courses)
    for index, course in enumerate(grades_df.columns):
        build_histogram(axes[index], grades_by_houses_df, course)

    for i in range(nb_courses, len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.show()


def histogram():
    try:
        dataset_df = parse_command_line()
        _loop_over_courses(dataset_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    histogram()
