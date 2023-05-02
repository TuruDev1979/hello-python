from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1, name="Juanjo", surname="González", age=43),
              User(id=2, name="Brais", surname="Moure", age=36),
              User(id=3, name="Gema", surname="Simon", age=45)]

router = APIRouter(tags=["users"],
                   responses={404: {"message":"No encontrado"}})

# GET
@router.get("/usersjson")
async def usersjson():
    return [{"name":"Juanjo","surname":"Gonzalez","age":43},
            {"name":"Brais","surname":"Moure","age":36},
            {"name":"Gema","surname":"Simon","age":45},]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}") # Path
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

@router.get("/userquery/") # Query
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    
# POST
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El suaurio ya existe")
    else:
        users_list.append(user)
        return {"aviso":"Usuario dado de alta"}
    
# PUT
@router.put("/user/")
async def user(user: User):
    found: bool = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        return {"error":"No se ha encontrado el usuario a actualizar"}
    else:
        return {"aviso":"Usuario actualizado"}

# DELETE
@router.delete("/user/{id}")
async def user(id: int):
    found: bool = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error":"No se ha encontrado el usuario a borrar"}
    else:
        return {"aviso":"Usuario eliminado"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}