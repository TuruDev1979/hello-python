from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1, name="Juanjo", surname="González", age=43),
              User(id=2, name="Brais", surname="Moure", age=36),
              User(id=3, name="Gema", surname="Simon", age=45)]

app = FastAPI()

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Juanjo","surname":"Gonzalez","age":43},
            {"name":"Brais","surname":"Moure","age":36},
            {"name":"Gema","surname":"Simon","age":45},]

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}