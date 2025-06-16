from fastapi import FastAPI
from pydantic import BaseModel  # usefull for validation
from typing import List



app = FastAPI()

class Student(BaseModel):
    id : int
    name : str
    email : str


students:List[Student] = [] 
