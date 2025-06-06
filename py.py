from pymongo import MongoClient
from json import load

json = open("/home/mas/Desktop/CEOS/JSON/metadados_exemplo.json")

class MongoIngestion:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.metadata_test

    def insert_data(self, fonte, entidade, json):
        fonte = fonte
        entidade = entidade
        fonte_entidade = f'{fonte}.{entidade}'
        json = load(json)
        self.collection = self.db[fonte_entidade]
        try:   
            self.collection.insert_one(json)
        except:
            print(f'Erro ao inserir o documento {json["title"]} na {fonte_entidade}')

mongo = MongoIngestion()
mongo.insert_data(fonte="teste", entidade="teste", json=json)
