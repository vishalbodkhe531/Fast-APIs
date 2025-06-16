from fastapi import FastAPI
from pydantic import BaseModel  # usefull for validation
from typing import List



app = FastAPI()

class Student(BaseModel):
    id : int
    name : str
    email : str


students:List[Student] = [] 



# decorators 
@app.get("/")
def readRoot():
    return {"message" : "Welcome To Python Fast-API"}


@app.get("/all-students")
def getStudents():
    return students

