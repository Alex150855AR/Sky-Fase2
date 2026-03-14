from fastapi import APIRouter, HTTPException
from typing import List
import json
import os
import uuid
from app.models import Cliente, ClienteCreate

router = APIRouter()
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "clientes.json")

def read_data() -> list:
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_data(data: list):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/api/clientes", response_model=List[Cliente])
def listar_clientes():
    return read_data()

@router.post("/api/clientes", response_model=Cliente, status_code=201)
def crear_cliente(cliente: ClienteCreate):
    data = read_data()
    nuevo_cliente = cliente.model_dump()
    nuevo_cliente["id"] = str(uuid.uuid4())
    data.append(nuevo_cliente)
    write_data(data)
    return nuevo_cliente

@router.get("/api/clientes/{client_id}", response_model=Cliente)
def obtener_cliente(client_id: str):
    data = read_data()
    for c in data:
        if c["id"] == client_id:
            return c
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.delete("/api/clientes/{client_id}")
def eliminar_cliente(client_id: str):
    data = read_data()
    for i, c in enumerate(data):
        if c["id"] == client_id:
            del data[i]
            write_data(data)
            return {"message": "Cliente eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
