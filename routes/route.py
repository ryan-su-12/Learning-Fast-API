from fastapi import APIRouter
from models.todos import Todo
from models.Finances import Finances
from config.database import collection_name
from config.database import finance_collection
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# get req method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

# post req method
@router.post("/")
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))

# update req method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})

# delete req method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

#### Finances section
@router.get("/finances")
async def get_finances():
    Finances = list_serial(finance_collection.find())
    return Finances

@router.post("/finaces")
async def post_finances(finances: Finances):
    finance_collection.insert_one(dict(finances))
