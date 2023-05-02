from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message":"No encontrado"}})

products_list = ["Producto1","Producto2","Producto3","Producto4"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]