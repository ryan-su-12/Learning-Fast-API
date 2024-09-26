from pydantic import BaseModel

class Finances(BaseModel):
    name: str
    job: str
    salary: int
    Yoe: int
