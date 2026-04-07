from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    major: str
    gpa: float

students = []

# GET
@app.get("/students")
def get_students():
    return students

# POST
@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return student

# PUT
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    students[student_id] = student
    return student

# PATCH
@app.patch("/students/{student_id}")
def patch_student(student_id: int, gpa: float):
    students[student_id].gpa = gpa
    return students[student_id]

# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return students.pop(student_id)
