# https://www.vultr.com/docs/how-to-create-a-restful-api-using-python-and-fastapi-3398/

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel # añadido en v02
class Student(BaseModel): # añadido en v02
    name: str
    age: int

from typing import Optional ## añadido en v05

app = FastAPI()

students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]

def student_check(student_id):
    if student_id not in range(0, len(students)):
        raise HTTPException(status_code=404, detail='Student Not Found')

@app.get('/students')  ## MODIFICADO EN V05
# def user_list():
#     return {'students': students}
def user_list(min: Optional[int] = None, max: Optional[int] = None):

    if min and max:
        # def filtraEdad(x):
        #     if min < x['age'] < max:
        #         return True
        #     return False
        #filtered_students = list(filter(filtraEdad, students))

        filtered_students = list(filter( lambda x: x['age'] in range(min,max), students))

        # filtered_students = list(
        #     filter(lambda student: max >= student['age'] >= min, students)
        # )
        return {'students': filtered_students}

    return {'students': students}


@app.get('/students/{student_id}')
def user_detail(student_id: int):
    student_check(student_id)
    return {'student': students[student_id]}  

# añadido en v02
@app.post('/students')
def user_add(student: Student):
    students.append(student)
    return {'student': students[-1]}  

@app.put('/students/{student_id}') # añadido en v3
def user_update(student: Student, student_id: int):
    student_check(student_id)
    students[student_id].update(student)
    return {'student': students[student_id]}

@app.delete('/students/{student_id}') # añadido en v4
def user_delete(student_id: int):
    student_check(student_id)
    del students[student_id]

    return {'students': students}