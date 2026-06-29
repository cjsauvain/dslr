import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

from tkinter import Tk
from matplotlib.axes import Axes
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.backends.backend_pdf import PdfPages
from src.metrics import (
    ft_precision,
    ft_recall,
    ft_f1_score,
    ft_accuracy,
    _HOUSES
)


_COL_WIDTH = 20
_HOUSE_COLORS = {
    "Gryffindor": "red",
    "Hufflepuff": "yellow",
    "Ravenclaw": "blue",
    "Slytherin": "green"
}
_COURSE_LABELS = {
    "Defense Against the Dark Arts":  "Defense Ag. the D.A",
    "Care of Magical Creatures":  "Care of M.C",
}


def _save_page_and_close(pdf: PdfPages):
    pdf.savefig()
    plt.close()


def _retrieve_correlations(
        grades_df: pd.DataFrame,
        nb_correlations: int | None = None
) -> pd.Series:
    corr = grades_df.corr().abs()
    mask = np.triu(np.ones(corr.shape, dtype=bool), k=1)
    corr = corr.where(mask)

    if nb_correlations is not None:
        return corr.stack().nlargest(nb_correlations).dropna()
    return pd.Series(corr.stack().dropna())


def _set_figure_and_axes(
        nrows: int,
        ncols: int,
        figure_title: str | None = None,
        house_colors_handles: list[Patch] | None = None,
        axes_labels_handles: list[Line2D] | None = None,
        screen_size_factor: float = 1.0
) -> np.ndarray:
    figure, axes = plt.subplots(nrows=max(1, nrows), ncols=max(2, ncols))
    if figure_title is not None:
        figure.suptitle(figure_title)

    if house_colors_handles is not None:
        figure.legend(
            handles=house_colors_handles,
            bbox_to_anchor=(0.94, 0.204),
            fontsize=18
        )
    if axes_labels_handles is not None:
        figure.legend(
            handles=axes_labels_handles,
            handlelength=0,
            handletextpad=0,
            bbox_to_anchor=(0.81, 0.131),
            fontsize=18
        )

    screen_resolution = Tk()
    dpi = figure.get_dpi()
    screen_width = screen_resolution.winfo_screenwidth() * screen_size_factor
    screen_height = screen_resolution.winfo_screenheight() * screen_size_factor
    figure.set_figwidth((screen_width * 0.99) / dpi)
    figure.set_figheight((screen_height * 0.93) / dpi)
    screen_resolution.destroy()

    return axes.flatten()


def _build_histogram(
        ax: Axes,
        grades_df: pd.DataFrame,
        course: str,
):
    for house in _HOUSES:
        house_grades_df = grades_df[grades_df["Hogwarts House"] == house]
        house_grades_df = house_grades_df.drop(
            columns="Hogwarts House",
            errors="ignore"
        )
        ax.hist(house_grades_df, color=_HOUSE_COLORS[house], alpha=0.5)
        ax.set_title(course)


def display_histograms(dataset_df: pd.DataFrame, pdf: PdfPages | None = None):
    grades_df = (
        dataset_df
        .select_dtypes("number")
        .drop(columns="Index", errors="ignore")
    )
    grades_df["Hogwarts House"] = dataset_df["Hogwarts House"]
    nb_courses = len(grades_df.columns) - 1
    house_colors_handles = [
        Patch(color=color, label=house, alpha=0.5)
        for house, color in _HOUSE_COLORS.items()
    ]
    axes_labels_handles = [
        Line2D([], [], color="none", label="X: Grades"),
        Line2D([], [], color="none", label="Y: # of students"),
    ]

    ncols = 5
    nrows = math.ceil(nb_courses / ncols)
    axes = _set_figure_and_axes(
        nrows,
        ncols,
        figure_title="Hogwarts Grade Distribution by Course",
        house_colors_handles=house_colors_handles,
        axes_labels_handles=axes_labels_handles
    )

    courses = [col for col in grades_df.columns if col != "Hogwarts House"]
    for index, course in enumerate(courses):
        _build_histogram(
            axes[index],
            grades_df[[course, "Hogwarts House"]],
            course
        )

    for i in range(nb_courses, len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    if pdf is not None:
        _save_page_and_close(pdf)
    else:
        plt.show()


def _build_scatter_plot(ax: Axes, grades_df: pd.DataFrame, courses: list[str]):
    x_course = courses[0]
    x_course = _COURSE_LABELS.get(x_course, x_course)
    ax.set_xlabel(x_course)

    y_course = courses[1]
    y_course = _COURSE_LABELS.get(y_course, y_course)
    ax.set_ylabel(y_course, rotation=80)

    for house in _HOUSES:
        house_grades_df = grades_df[grades_df["Hogwarts House"] == house]
        ax.scatter(
            house_grades_df[courses[0]],
            house_grades_df[courses[1]],
            color=_HOUSE_COLORS[house]
        )


def display_scatter_plots(
        dataset_df: pd.DataFrame,
        nb_correlations: int | None = None,
        pdf: PdfPages | None = None
):
    grades_df = (
        dataset_df
        .select_dtypes(include="number")
        .drop(columns="Index")
    )
    grades_df["Hogwarts House"] = dataset_df["Hogwarts House"]
    correlations = _retrieve_correlations(
        grades_df.drop(columns="Hogwarts House"),
        nb_correlations
    )

    nrows, ncols = (2, 3) if nb_correlations is not None else (4, 4)
    page_size = nrows * ncols
    correlations = correlations.index

    for start in range(0, len(correlations), page_size):
        page = correlations[start:start + page_size]
        title = "Feature correlations" if pdf else "Most correlated features"
        axes = _set_figure_and_axes(nrows, ncols, figure_title=title)

        for index, courses in enumerate(page):
            _build_scatter_plot(axes[index], grades_df, courses)

        for i in range(len(page), len(axes)):
            axes[i].set_visible(False)

        plt.tight_layout()
        if pdf is not None:
            _save_page_and_close(pdf)

    if pdf is None:
        plt.show()


def _display_metrics_header():
    print("\n", f"{'':<{_COL_WIDTH // 2}}", end="")
    for column in ["Precision", "Recall", "F1-score", "Support"]:
        print(f"{column:>{_COL_WIDTH - 6}}", end="")
    print()


def _display_house_metrics(
        house: str,
        precision: float,
        recall: float,
        f1_score: float,
        support: int
):
    print(f"{house:<{_COL_WIDTH // 2}}", end="")
    for value in [precision, recall, f1_score]:
        print(f"{value:>{_COL_WIDTH - 6}.2f}", end="")
    print(f"{support:>{_COL_WIDTH - 6}}")


def display_metrics(confusion_matrix: np.ndarray):
    print("\nMETRICS:\n--------")
    print(f"\nAccuracy: {ft_accuracy(confusion_matrix):.2f}")
    _display_metrics_header()
    for house_index, house in enumerate(_HOUSES):
        precision = ft_precision(confusion_matrix, house_index)
        recall = ft_recall(confusion_matrix, house_index)
        f1_score = ft_f1_score(precision, recall)
        _display_house_metrics(
            house,
            precision,
            recall,
            f1_score,
            confusion_matrix[house_index].sum()
        )


def display_confusion_matrix(confusion_matrix: np.ndarray):
    confusion_matrix_df = pd.DataFrame(
        confusion_matrix,
        index=_HOUSES,
        columns=_HOUSES
    )
    confusion_matrix_df.index.name = "True"
    confusion_matrix_df.columns.name = "Predicted"
    print("\nCONFUSION MATRIX:\n-----------------\n\n", confusion_matrix_df)


def display_learning_curves(cost_histories: dict):
    axes = _set_figure_and_axes(
        nrows=2,
        ncols=2,
        figure_title="Learning Curves per House",
        screen_size_factor=0.7
    )

    for index, house in enumerate(cost_histories):
        house_cost_history = cost_histories[house]
        training_loss = house_cost_history["training"]
        axes[index].plot(
            range(len(training_loss)),
            training_loss,
            color=_HOUSE_COLORS[house],
            label=house
        )

        validation_loss = house_cost_history["validation"]
        if len(validation_loss) != 0:
            axes[index].plot(
                range(len(validation_loss)),
                validation_loss,
                color="purple",
                label="Validation"
            )

        axes[index].set_xlabel("Iteration")
        axes[index].set_ylabel("Cost")
        axes[index].legend()

    plt.show()
