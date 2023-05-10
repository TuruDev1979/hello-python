from fastapi import APIRouter, HTTPException
from db.models.user import User

router = APIRouter(prefix="/userdb", 
                   tags=["userdb"],
                   responses={404: {"message":"No encontrado"}})

users_list = []

@router.get("/")
async def users():
    return users_list

@router.get("/{id}") # Path
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

@router.get("/") # Query
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    
# POST
@router.post("/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El suaurio ya existe")
    else:
        users_list.append(user)
        return {"aviso":"Usuario dado de alta"}
    
# PUT
@router.put("/")
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
@router.delete("/{id}")
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