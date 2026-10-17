from src.evaluation import run_validation_and_metrics
from src.logreg import logreg
from src.model_io import write_to_model_json_file
from src.parsing import training_parsing
from src.preprocessing import dataset_preprocessing
from src.visualization import display_learning_curves


def train():
    try:
        args = training_parsing()
        train_df, validation_df, medians = dataset_preprocessing(
            args.dataset, args.validation_ratio
        )

        json_content, means, stds, cost_histories = logreg(
            train_df, validation_df, medians, args.learning_curve
        )
        write_to_model_json_file(json_content)

        if args.validation_ratio > 0 and validation_df is not None:
            run_validation_and_metrics(
                validation_df,
                json_content["weights"],
                means,
                stds,
                args.confusion_matrix,
                args.metrics,
            )

        if args.learning_curve and cost_histories is not None:
            display_learning_curves(cost_histories)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    train()
