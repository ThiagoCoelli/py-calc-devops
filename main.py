from fastapi import FastAPI
import pandas

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Docker + FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
