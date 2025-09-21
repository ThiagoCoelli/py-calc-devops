from src.main import *
from fastapi import FastAPI



def teste_root():
    assert read_root() == {"message": "Hellow Word!"}


def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
