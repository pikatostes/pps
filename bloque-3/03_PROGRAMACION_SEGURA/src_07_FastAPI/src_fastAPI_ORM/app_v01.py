from fastapi import FastAPI, HTTPException

import schemas
import db
from modelsDB import Student

db.Base.metadata.create_all(db.engine)

# Añade Datos iniciales a la tabla
lista = [("Ana", 44), ("Ricardo", 37), ("Marina", 32)]
for x in lista:
    db.session.add(Student(x[0], x[1]))
db.session.commit()


app = FastAPI()

@app.get('/students/', response_model=list[schemas.StudentOut])  
def user_list():
    res = db.session.query(Student).all()
    return res

@app.post('/students/', response_model=schemas.StudentOut)  
def user_add(alu: schemas.StudentIn):
    new = Student(alu.name, alu.age)
    db.session.add(new)
    db.session.commit()
    return db.session.query(Student).get(new.id)