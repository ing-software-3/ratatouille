from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List
from app.models.pedido import PedidoCreate, PedidoResponse

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

# Base de datos simulada en memoria
PEDIDOS_DB = []

@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def realizar_pedido(pedido: PedidoCreate):
    """
    HTTP POST: Caso de uso 'Realizar pedido'. 
    Simula el cálculo automático del total y la comisión de la plataforma (10%).
    """
    nuevo_id = len(PEDIDOS_DB) + 1
    
    # Valores simulados basados en las reglas de tu doc
    total_simulado = 35000.0  
    comision_simulada = total_simulado * 0.10  # PorcentajeGanancia de la plataforma
    
    nuevo_pedido = {
        "id": nuevo_id,
        "fecha": date.today(),
        "estado": "Pendiente",
        "total": total_simulado,
        "comision": comision_simulada,
        **pedido.model_dump()
    }
    
    PEDIDOS_DB.append(nuevo_pedido)
    return nuevo_pedido

@router.put("/{pedido_id}/direccion", response_model=PedidoResponse)
def actualizar_direccion_entrega(pedido_id: int, nueva_direccion: str):
    """
    HTTP PUT: Caso de uso 'Actualizar dirección de entrega'.
    Modifica una propiedad específica de un pedido existente.
    """
    for p in PEDIDOS_DB:
        if p["id"] == pedido_id:
            p["direccion_entrega"] = nueva_direccion
            return p
    raise HTTPException(status_code=404, detail="Pedido no encontrado")

@router.delete("/{pedido_id}")
def cancelar_pedido(pedido_id: int):
    """
    HTTP DELETE: Caso de uso 'Cancelar pedido'. Mueve el estado a 'Cancelado'.
    """
    for p in PEDIDOS_DB:
        if p["id"] == pedido_id:
            p["estado"] = "Cancelado"
            return {"message": f"Pedido {pedido_id} cancelado con éxito", "estado": p["estado"]}
    raise HTTPException(status_code=404, detail="Pedido no encontrado")