from google.oauth2 import service_account
from google.cloud import firestore
import json
import os


service_account_file = "C:/Users/claytong/.gcloudsk/adaptativo-pv.json"

try:
    cred = service_account.Credentials.from_service_account_file(service_account_file)
    db = firestore.Client(credentials=cred)
except Exception as e:
    print(f"Erro ao carregar o cliente ou as credenciais do firestore: {e}")
    exit()

def save_to_firestore_collection(collection_id, data):
    collection_ref = db.collection(collection_id)
    for doc_id, doc_data in data.items():
        collection_ref.document(doc_id).set(doc_data)

def choose_file_and_get_json():
    print("\nArquivos collection JSON encontrados:")
    files = [arq for arq in os.listdir("./") if arq.startswith("collection") and arq.endswith(".json")]
    for number, arquivo in enumerate(files, 0):
        print(f"  {number}. {arquivo}")
    while True:
        try:
            escolha = input("\nEscolha um número de arquivo ou 's' para sair: ")
            if escolha == "s" or escolha == "S":
                return None
            if -1 < int(escolha) < len(files):
                with open(files[int(escolha)], 'r') as file:
                    print(f"Carregando dados do arquivo '{files[int(escolha)]}'..")
                    return json.load(file)
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")


collections = choose_file_and_get_json()

if collections is not None:
    for collection_id_name, collection_data in collections.items():
        save_to_firestore_collection(collection_id_name, collection_data)
    print("Dados carregados, enviados e importados para o Firestore.\n")
else:
    print("Processo não realizado.\n")
