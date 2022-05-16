from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

students = []

class Student(BaseModel):
    id: str
    name: str
    lastname: str
    skills: List[str]=[]


@app.get('/')
def mensajes():
    return {"Hola": "World!"}

@app.get('/login')
def mensajes2():
    return "Ingrese sus datos en el servidor"

@app.get('/users/{user_id}')
def mensajes3(user_id:int):
    return f"El user id es {user_id}"

@app.get('/students')
def getStudents():
    return students

@app.get('/students/{id}')
def getStudent(id:str):
    for student in students:
        if student["id"] == id:
            return student
    return "Estudiante no existe"

@app.put('/students/{id}')
def updateStudent(updatedStudent:Student, id:str):
    for student in students:
        if student["id"] == id:
            student["name"] = updatedStudent.name
            student["lastname"] = updatedStudent.lastname
            student["skills"] = updatedStudent.skills
            return "Estudiante actualizado"
    return "Estudiante no existe"

@app.delete('/students/{id}')
def deleteStudent(id:str):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return "Estudiante eliminado"
    return "Estudiante no existe"

@app.post('/students')
def saveStudent(student:Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return f"Estudiante creado"
    # return f"Estudiante {student.name} {student.lastname}: {student.skills} guardado!"