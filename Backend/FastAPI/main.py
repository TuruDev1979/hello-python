from fastapi import FastAPI
from routers import products, users, basic_auth_user, jwt_auth_user
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_user.router)
app.include_router(jwt_auth_user.router)

app.mount("/static",StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}

