import pytest
import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
TEST_DATA_FILE = "data/clientes.json"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_crear_cliente_valido():
    payload = {
        "nombre": "Juan Perez", "email": "juan@example.com",
        "rfc": "ABCD123456XYZ", "telefono": "5512345678"
    }
    response = client.post("/api/clientes", json=payload)
    assert response.status_code == 201

def test_crear_cliente_rfc_invalido():
    payload = {
        "nombre": "Ana Gomez", "email": "ana@example.com",
        "rfc": "RFCINVALIDO", "telefono": "5512345678"
    }
    response = client.post("/api/clientes", json=payload)
    assert response.status_code == 422
