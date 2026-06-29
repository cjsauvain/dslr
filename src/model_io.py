import json


_MODEL_PATH = "model.json"


def write_to_model_json_file(json_content: dict):
    with open(_MODEL_PATH, "w") as file:
        json.dump(json_content, file, indent=4)
