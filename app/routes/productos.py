from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from app.models.producto import ProductoCreate, ProductoResponse

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# Base de datos simulada en memoria por ahora
DE_PRUEBA_DB = []

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(categoria: Optional[str] = None):
    """
    HTTP GET: Obtiene todos los productos. Permite filtrar por categoría para las recomendaciones.
    """
    if categoria:
        return [p for p in DE_PRUEBA_DB if p["categoria"].lower() == categoria.lower()]
    return DE_PRUEBA_DB

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_nuevo_producto(producto: ProductoCreate):
    """
    HTTP POST: Guarda un nuevo producto en el menú del restaurante.
    """
    nuevo_id = len(DE_PRUEBA_DB) + 1
    # Convertimos el modelo de Pydantic a diccionario de Python y le asignamos un ID
    producto_guardado = {"id": nuevo_id, **producto.model_dump()}
    DE_PRUEBA_DB.append(producto_guardado)
    return producto_guardado