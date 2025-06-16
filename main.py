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

@app.post("/all-students")
def addStudent(student : Student):
    students.append(student)
    return student



@app.put("/update-student/{studentId}")
def updateStudent(studentId:int,updatedStudent : Student):
    for index,item in enumerate(students):
        if item.id == studentId:
            students[index] = updatedStudent
            return updatedStudent
    return {"Error" : "Student not found !!"}    


