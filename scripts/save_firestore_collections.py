from proc.firebase import get_firestore_db, get_json_from_firestore_collection_list
from proc.converters import convert_date_time_to_string
from proc.file import write_json_file, read_json_file

config = read_json_file("../config.json")

db = get_firestore_db(config)

json_data = get_json_from_firestore_collection_list(db)

data_hora = convert_date_time_to_string(None)
json_file_name = f"collections_{data_hora}.json"

write_json_file(json_file_name, json_data)

print(f"Dados do Firestore exportados, baixados e salvos no arquivo: {json_file_name}")
