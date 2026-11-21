from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_crear_producto():
    r = cliente.post("/productos", json={"nombre": "Arroz", "precio": 4.5, "stock": 20})
    assert r.status_code == 201
    assert r.json()["nombre"] == "Arroz"

def test_producto_no_existe():
    assert cliente.get("/productos/999").status_code == 404
