from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.conection import db_conection
from bson import ObjectId

router = APIRouter(prefix="/userdb", 
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message":"No encontrado"}})


# GET
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_conection.users.find())

@router.get("/{id}") # Path
async def user(id: str):
    try:
        return search_user(field="_id", value=ObjectId(id))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El suaurio no existe")
    
# POST -- Insertar
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
#    if type(search_user_by_username(user.username)) == User:
    if type(search_user(field="username",value=user.username)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El suaurio ya existe")
    else:
        user_dict = dict(user)
        del user_dict["id"]

        id = db_conection.users.insert_one(user_dict).inserted_id
        new_user = user_schema(db_conection.users.find_one({"_id": id}))

        return User(**new_user)
    
# PUT -- Actualizar
@router.put("/", response_model=User, status_code=status.HTTP_200_OK)
async def user(user: User):
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_conection.users.find_one_and_replace(filter={"username": user.username},replacement=user_dict)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El suaurio no existe")
    
    return search_user(field="username",value=user.username)

# DELETE -- Borrar
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_conection.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El suaurio no existe")
    
####################   FUNCIONES   ####################
def search_user(field: str, value):
    try:
        user = db_conection.users.find_one({field: value})
        return User(**user_schema(user))
    except:
        return {"error":"No se ha encontrado el usuario"}