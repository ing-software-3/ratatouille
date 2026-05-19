from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel  # <-- Necesitamos importar esto para el molde seguro
from typing import Optional

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios / Inteligencia Artificial"]
)

# 1. Creamos el molde (Schema) para que los datos viajen ocultos en el Body
class LoginRequest(BaseModel):
    correo: str
    contrasenia: str

# 2. Modificamos el login para que reciba el molde
@router.post("/login")
def iniciar_sesion(datos: LoginRequest):  # <-- Ahora lee el JSON seguro
    """
    HTTP POST: Caso de uso 'Iniciar sesión'.
    Validación segura de credenciales del usuario en el Body.
    """
    # Ahora accedemos a los datos usando el punto (datos.correo y datos.contrasenia)
    if datos.correo == "sebastian@ratatouille.com" and datos.contrasenia == "123456":
        return {"login": True, "message": "Bienvenido a Ratatouille", "usuario_id": 1}
    
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# 3. Tu método de recomendaciones se queda exactamente igual
@router.get("/{cliente_id}/recomendaciones")
def recibir_recomendaciones(cliente_id: int, algoritmo: Optional[str] = "clasificacion_preferencias"):
    """
    HTTP GET: Caso de uso 'Recibir recomendaciones'.
    Simula el procesamiento del dataset de comidas rápidas mediante Machine Learning.
    """
    return {
        "cliente_id": cliente_id,
        "algoritmo_aplicado": algoritmo,
        "objetivo": "Optimizar factores como gustos e ingredientes nutricionales",
        "comidas_recomendadas": [
            {"id": 1, "nombre": "Hamburguesa Gourmet Inteligente", "probabilidad_gusto": "94%"},
            {"id": 3, "nombre": "Pizza Familiar Baja en Calorías", "probabilidad_gusto": "88%"}
        ]
    }