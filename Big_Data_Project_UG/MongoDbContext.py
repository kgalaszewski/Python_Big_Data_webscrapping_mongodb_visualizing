import pymongo
from pymongo import MongoClient
from typing import List
from AppSettings import AppSettings


class DBContext:
    def __init__(self,
                mongo_hostname: str = AppSettings.MONGO_HOSTNAME,
                mongo_port: int = AppSettings.MONGO_PORT,
                mongo_clustername: str = AppSettings.MONGO_CLUSTERNAME):
        self.__host = mongo_hostname
        self.__port = mongo_port
        self.__client = MongoClient(self.__host, self.__port)
        self.__db = self.__client[mongo_clustername]
        self.__collection = None


    def add_rows(self, rows: list, collection_name: str):
        self.__initialize_collection(collection_name)

        if rows:
            try:
                self.__collection.insert_many(rows)
                print(f'Inserted {len(rows)} rows to the db collection')
            except Exception as ex:
                print(f'Could not insert rows due to : {str(ex)}')


    def add_row(self, row, collection_name: str):
        self.__initialize_collection(collection_name)

        if row:
            print('Adding new row')
            try:
                self.__collection.insert_one(row)
            except Exception as ex:
                print(f'Could not insert row due to : {str(ex)}')

    def get_by_Id(self, id: int, collection_name: str) -> dict:
        self.__initialize_collection(collection_name)

        try:
            print(f'Reading element with id : {id}')
            result = dict(self.__collection.find_one({"_id": f"{id}"}))

            if result:
                return result
            else:
                print(f'Could not find the record with id : {id}')
        except Exception as ex:
            print(f'Reading element from db was interrupted by : {str(ex)}')

    def get_all(self, collection_name: str) -> List[dict]:
        self.__initialize_collection(collection_name)

        try:
            all_elements = self.__collection.find()
            result = list(map(lambda cursor: dict(cursor), all_elements))

            if result:
                return result
            else:
                print('Colelction is empty')
        except Exception as ex:
            print(f'Reading all documents from collection was interrupted by : {str(ex)}')
        finally:
            print(f'Successfuly read {len(result)} elements from the collection')


    def drop_collection(self, collection_name: str):
        self.__initialize_collection(collection_name)
        
        try:
            print('Dropping collection')
            self.__collection.drop()
        except Exception as ex:
            print(f'Could not clear the collection due to {str(ex)}')
        finally:
            print('Dropping job done')

    
    def __initialize_collection(self, collection_name: str = AppSettings.COLLECTION_NAME):
        print(f'Initializing the collection in DB. Collection name={collection_name}')
        self.__collection = self.__db[collection_name]
