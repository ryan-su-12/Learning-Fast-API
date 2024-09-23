import os
from fastapi import FastAPI
from routes.route import router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(router)


from pymongo.mongo_client import MongoClient
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("You have successfully connected to MongoDB!")
except Exception as e:
        print(e)
