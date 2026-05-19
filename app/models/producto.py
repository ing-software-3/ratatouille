from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    disponible: bool = True
    categoria: str

class ProductoCreate(ProductoBase):
    pass  # Lo que se necesita para crear un producto

class ProductoResponse(ProductoBase):
    id: int  # Cuando responde la API o MySQL, ya incluye el ID generado

    class Config:
        from_attributes = True