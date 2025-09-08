from fastapi import FastAPI

# Cria a aplicação
app = FastAPI()

# Rota inicial
@app.get("/")
def read_root():
    return {"message": "Hello, Docker + FastAPI!"}

# Exemplo de rota com parâmetro
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}