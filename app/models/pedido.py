from pydantic import BaseModel
from datetime import date, time
from typing import List

class PedidoBase(BaseModel):
    cliente: str
    direccion_entrega: str
    hora_entrega: time
    productos: List[int]  # Lista de IDs de los productos que compra

class PedidoCreate(PedidoBase):
    pass

class PedidoResponse(PedidoBase):
    id: int
    fecha: date
    estado: str  # "Pendiente", "Aceptado", "Cancelado"
    total: float
    comision: float

    class Config:
        from_attributes = True