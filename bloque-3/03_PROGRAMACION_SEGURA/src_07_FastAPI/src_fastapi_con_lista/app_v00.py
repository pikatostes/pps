# https://www.vultr.com/docs/how-to-create-a-restful-api-using-python-and-fastapi-3398/


from fastapi import FastAPI

app = FastAPI()

students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]

@app.get('/students')
def user_list():
    return {'students': students}