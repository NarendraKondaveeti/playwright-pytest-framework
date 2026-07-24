from pathlib import Path
import json


class JsonReader:

    @staticmethod
    def read_json(file_path):

        project_root = Path(__file__).resolve().parent.parent
        full_path = project_root / file_path

        with open(full_path, "r", encoding="utf-8") as file:
            return json.load(file)