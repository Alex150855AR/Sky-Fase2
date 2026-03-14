from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="SKY API - Fase 2", description="Microservicio de Clientes")
app.include_router(router)
