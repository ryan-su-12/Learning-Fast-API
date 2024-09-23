from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    desc: str
    complete: bool