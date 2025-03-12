from google.oauth2 import service_account
from google.cloud import firestore


def get_firestore_db (config):
    saf = config.firebase_service_account_json_api_key_path
    try:
        cred = service_account.Credentials.from_service_account_file(saf)
        db = firestore.Client(credentials=cred)
    except Exception as e:
        print(f"Erro na conexão com Firestore: {e}")
        exit()
    return db

def get_json_data_from_firestore_collection(db: firestore.Client, collection):
    collection_docs_list = list(db.collection(collection.id).stream())
    if collection_docs_list:
        return { doc.id: doc.to_dict() for doc in collection_docs_list }
    else:
        return {}

def get_json_from_firestore_collection_list (db: firestore.Client):
    json_data = {}
    for collection in db.collections():
        json_data[collection.id] = get_json_data_from_firestore_collection(db, collection)
    return json_data

