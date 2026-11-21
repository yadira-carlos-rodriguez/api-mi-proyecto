from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Productos")

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

productos = {}
siguiente_id = 1

@app.get("/")
def inicio():
    return {"mensaje": "API de Bodega funcionando"}

@app.get("/productos")
def listar():
    return productos

@app.get("/productos/{id}")
def obtener(id: int):
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos[id]

@app.post("/productos", status_code=201)
def crear(producto: Producto):
    global siguiente_id
    productos[siguiente_id] = producto.model_dump()
    siguiente_id += 1
    return {"id": siguiente_id - 1, **producto.model_dump()}

@app.put("/productos/{id}")
def actualizar(id: int, producto: Producto):
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    productos[id] = producto.model_dump()
    return productos[id]

@app.delete("/productos/{id}", status_code=204)
def eliminar(id: int):
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    del productos[id]
