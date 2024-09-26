from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)

db = client.todo_db

collection_name = db["todo_collection"]

finance_collection = db["finance collection"]

