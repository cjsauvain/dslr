import math
from tkinter import Tk
from numpy import ndarray
from pandas import DataFrame
from src.parsing import parse_command_line
from src.plot import build_histogram
from matplotlib import patches, pyplot as plt


def _get_grades_by_houses(dataset_df: DataFrame) -> dict[str, DataFrame]:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    return {
        house: dataset_df[dataset_df["Hogwarts House"] == house]
            .select_dtypes("number")
            .drop(columns="Index", errors="ignore")
            for house in houses
    }


def _set_figure_and_axes(nb_courses: int, nb_columns: int = 5) -> tuple[ndarray, int]:
    nb_rows = math.ceil(nb_courses / nb_columns)

    figure, axes = plt.subplots(nrows=nb_rows, ncols=nb_columns)
    figure.suptitle("Hogwarts Grade Distribution by Course")
    handles = [
        patches.Patch(color="red", label="Gryffindor", alpha=0.5),
        patches.Patch(color="yellow", label="Hufflepuff", alpha=0.5),
        patches.Patch(color="blue", label="Ravenclaw", alpha=0.5),
        patches.Patch(color="green", label="Slytherin", alpha=0.5)
    ]
    figure.legend(handles=handles, loc="lower right", fontsize=18)
    axes = axes.flatten()

    screen_resolution = Tk()
    dpi = figure.get_dpi()
    screen_width = screen_resolution.winfo_screenwidth()
    screen_height = screen_resolution.winfo_screenheight()
    figure.set_figwidth((screen_width * 0.95) / dpi)
    figure.set_figheight((screen_height * 0.90) / dpi)
    screen_resolution.destroy()

    return axes, nb_columns


def _loop_over_courses(dataset_df: DataFrame):
    houses_colors = {
        "Gryffindor": "red",
        "Hufflepuff": "yellow",
        "Ravenclaw": "blue",
        "Slytherin": "green"
    }
    grades_df = dataset_df.select_dtypes("number").drop(columns="Index", errors="ignore")
    grades_by_houses_df = _get_grades_by_houses(dataset_df)
    nb_courses = len(grades_df.columns)
    axes, nb_columns = _set_figure_and_axes(nb_courses)

    last_row = (nb_courses // nb_columns) + 1
    last_row_start = (last_row - 1) * nb_columns
    nb_axes_last_row = nb_courses % nb_columns
    above_empty_axes_start = (last_row - 2) * nb_columns + nb_axes_last_row
    above_empty_axes_end = (last_row - 1) * nb_columns
    for index, course in enumerate(grades_df.columns):

        is_on_last_row = index >= last_row_start

        for house, grades in grades_by_houses_df.items():
            if nb_courses % nb_columns == 0:
                is_above_empty_axes = False
            else:
                is_above_empty_axes =  above_empty_axes_start <= index <= above_empty_axes_end
            set_xlabel = is_on_last_row or is_above_empty_axes
            set_ylabel = index % nb_columns == 0

            build_histogram(axes[index], grades[course], course, houses_colors[house], set_xlabel, set_ylabel)

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
