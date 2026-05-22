import math
from tkinter import Tk
import numpy as np
from matplotlib import patches, pyplot as plt
import pandas as pd


def _set_figure_and_axes(nb_courses: int, nb_columns=5) -> np.ndarray:
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

    return axes


def display_histograms(gryffindor_df: pd.DataFrame, hufflepuff_df: pd.DataFrame, ravenclaw_df: pd.DataFrame, slytherin_df: pd.DataFrame):
    gryffindor_grades_df = gryffindor_df.select_dtypes(include="number").drop(columns="Index")
    hufflepuff_grades_df = hufflepuff_df.select_dtypes(include="number").drop(columns="Index")
    ravenclaw_grades_df = ravenclaw_df.select_dtypes(include="number").drop(columns="Index")
    slytherin_grades_df = slytherin_df.select_dtypes(include="number").drop(columns="Index")

    nb_courses = len(gryffindor_grades_df.columns)

    axes = _set_figure_and_axes(nb_courses)

    for index, course in enumerate(gryffindor_grades_df.columns):

        gryffindor_grades_list = gryffindor_grades_df[course].dropna().values
        hufflepuff_grades_list = hufflepuff_grades_df[course].dropna().values
        ravenclaw_grades_list = ravenclaw_grades_df[course].dropna().values
        slytherin_grades_list = slytherin_grades_df[course].dropna().values
        
        axes[index].hist(gryffindor_grades_list, color="red", alpha=0.5)
        axes[index].hist(hufflepuff_grades_list, color="yellow", alpha=0.5)
        axes[index].hist(ravenclaw_grades_list, color="blue", alpha=0.5)
        axes[index].hist(slytherin_grades_list, color="green", alpha=0.5)

        axes[index].set_title(course)
        axes[index].set_xlabel("grades")
        axes[index].set_ylabel("# of students")
    
    for i in range(nb_courses, len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.show()


def display_scatter_plot(dataset_df: pd.DataFrame):
    pass