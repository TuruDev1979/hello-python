from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
SECRET = "6f969970ca005a43006229e2d339e1194662bc1e2a539852c3b29d869a5066bf"

crypt = CryptContext(schemes="bcrypt")

router = APIRouter(prefix="/jwt_auth_user",
                   tags=["jwt_auth_user"],
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
        "password":"$2a$12$hzjjmZW3kLWGAeHnA8FywulShEfWkkgNYqVk3k8MEug.GAsj39XXS"
    },
    "turudev": {
        "username":"turudev",
        "full_name":"Juanjo González",
        "email":"jjgonzalez.agudo@gmail.com",
        "disabled":True,
        "password":"$2a$12$7pKxmhWd429InmTxXG.LLu8iv77rRZSFJpKIILJW96KD31m4WB5PO"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def authenticate_user(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token=token, key=SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="Credenciales de autenticación inválidas", 
                                headers={"www-Authenticate": "Bearer"})
        
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"www-Authenticate": "Bearer"})

    return search_user(username)

async def current_user(user: User = Depends(authenticate_user)):    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Usuario inactivo", 
                            headers={"www-Authenticate": "Bearer"})
    
    return user

@router.post("/login2")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if not users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto")

    user = search_user_db(form.username)
  
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="La contraseña no es correcta") 
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = {"sub":user.username, 
                    "exp": expire}

    return {"access_token": jwt.encode(claims=access_token, key=SECRET, algorithm=ALGORITHM), "token_type":"bearer"}

@router.get("/users2/me")
async def me(user: User = Depends(current_user)):
    return user