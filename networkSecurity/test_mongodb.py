from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
uri = os.getenv("MONGO_DB_URI") or os.getenv("MONGO_DB_URL")
if not uri:
    raise ValueError("MONGO_DB_URI or MONGO_DB_URL environment variable is required to connect to MongoDB.")
client = MongoClient(uri, serverSelectionTimeoutMS=30000, connectTimeoutMS=10000)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)