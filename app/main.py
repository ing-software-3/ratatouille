from fastapi import FastAPI
# Importamos todos los módulos de rutas
from app.routes import productos, pedidos, usuarios 

app = FastAPI(
    title="Ratatouille",
    description="Backend modular para gestión de pedidos y recomendaciones de comida rápida",
    version="1.0.0"
)

# Conectamos las rutas de forma organizada al core de FastAPI
app.include_router(productos.router)
app.include_router(pedidos.router)
app.include_router(usuarios.router)

@app.get("/")
def read_root():
    return {"status": "Online", "app": "Ratatouille Marketplace API"}