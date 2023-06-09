from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# OAuth2PasswordBearer Gestiona la autenticación.
# OAuth2PasswordRequestForm Forma en la se va a enviar a la api los criterios de autentificación.

router = APIRouter(prefix="/basic_auth_user",
                   tags=["basic_auth_user"],
                   responses={404: {"message":"No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev": {
        "username":"mouredev",
        "full_name":"Brais Moure",
        "email":"braismoure@mouredev.com",
        "disabled":False,
        "password":"123456"
    },
    "turudev": {
        "username":"turudev",
        "full_name":"Juanjo González",
        "email":"jjgonzalez.agudo@gmail.com",
        "disabled":True,
        "password":"654321"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"www-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Usuario inactivo", 
                            headers={"www-Authenticate": "Bearer"})
    
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="La contraseña no es correcta") 
    
    return {"access_token": user.username , "token_type":"bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user