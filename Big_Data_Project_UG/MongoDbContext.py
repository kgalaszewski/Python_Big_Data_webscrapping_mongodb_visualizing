import pymongo
from pymongo import MongoClient
from typing import List
from AppSettings import AppSettings


class DBContextTempName:  # TODO change name so that its context like DonkeyDb
    def __init__(self,
                mongo_hostname: str = AppSettings.MONGO_HOSTNAME,
                mongo_port: int = AppSettings.MONGO_PORT,
                mongo_clustername: str = AppSettings.MONGO_CLUSTERNAME):
        self.__host = mongo_hostname
        self.__port = mongo_port
        self.__client = MongoClient(self.__host, self.__port)
        self.__db = self.__client[mongo_clustername]
        self.__collection = None

    # TODO move to the end ? its a private method
    def __initialize_collection(self, collection_name: str = AppSettings.COLLECTION_NAME):
        if self.__collection is None:
            print(f'Initializing the collection in DB. Collection name={collection_name}')
            self.__collection = self.__db[collection_name]


    def add_tempnames(self, rows: list): # TODO change name to something like add_donkey
        self.__initialize_collection()

        if rows:
            try:
                self.__collection.insert_many(rows)
                print(f'Inserted {len(rows)} rows to the db collection')
            except Exception as ex:
                print(f'Could not insert rows due to : {str(ex)}')


    def add_onetempname(self, row): # TODO name
        self.__initialize_collection()

        if row:
            print('Adding new row')
            try:
                self.__collection.insert_one(row)
            except Exception as ex:
                print(f'Could not insert row due to : {str(ex)}')

        
    def get_by_Id(self, id: int) -> dict: #TODO parameter name check if valid
        self.__initialize_collection()

        try:
            print(f'Reading element with id : {id}')
            result = dict(self.__collection.find_one({"_id": f"{id}"}))

            if result:
                return result
            else:
                print(f'Could not find the record with id : {id}') # TODO should I return empty just for program not to crash ?
        except Exception as ex:
            print(f'Reading element from db was interrupted by : {str(ex)}')

            
    def get_all(self) -> List[dict]:  # TODO parameter name check if valid
        self.__initialize_collection()

        try:
            all_elements = self.__collection.find()
            result = list(map(lambda cursor: dict(cursor), all_elements))

            if result:
                return result
            else:
                print('Colelction is empty')  # TODO should I return empty just for program not to crash ?
        except Exception as ex:
            print(f'Reading all documents from collection was interrupted by : {str(ex)}')
        finally:
            print(f'Successfuly read {len(result)} elements from the collection')


    def drop_collection(self):
        self.__initialize_collection()
        
        try:
            print('Dropping collection')
            self.__collection.drop()
        except Exception as ex:
            print(f'Could not clear the collection due to {str(ex)}')
        finally:
            print('Dropping job done')
