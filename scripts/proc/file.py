from converters import convert_datetime
import json

def read_json_file (file_name):
    return json.load(file_name)

def write_json_file (file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False, default=convert_datetime)
