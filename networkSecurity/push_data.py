import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()
uri = os.getenv("MONGO_DB_URI") or os.getenv("MONGO_DB_URL")
import certifi
ca = certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logger

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = json.loads(data.T.to_json()).values()
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            if not uri:
                raise CustomException("MONGO_DB_URI or MONGO_DB_URL environment variable is not set.", sys)
            self.database = database
            self.collection = collection
            self.records = records
            self.mongoclient = pymongo.MongoClient(
                uri,
                serverSelectionTimeoutMS=30000,
                connectTimeoutMS=10000,
            )
            self.mongoclient.admin.command("ping")
            self.database = self.mongoclient[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "network_security"
    COLLECTION = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(FILE_PATH)
    print('records',records)
    no_of_records = networkobj.insert_data_to_mongodb(records,DATABASE,COLLECTION)
    print(f"{no_of_records} records inserted successfully")
    
           