from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.conection import db_conection

router = APIRouter(prefix="/userdb", 
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message":"No encontrado"}})

users_list = []





# GET
@router.get("/", response_model=list(User))
async def users():
    return users_schema(db_conection.local.users.find())

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
    
# POST -- Insertar
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user_by_username(user.username)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El suaurio ya existe")
    else:
        user_dict = dict(user)
        del user_dict["id"]

        id = db_conection.local.users.insert_one(user_dict).inserted_id
        new_user = user_schema(db_conection.local.users.find_one({"_id": id}))

        return User(**new_user)

# PUT -- Actualizar
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


def search_user_by_username(username: str):
    try:
        user = db_conection.local.users.find_one({"username": username})
        return User(**user_schema(user))
    except:
        return {"error":"No se ha encontrado el usuario"}
        