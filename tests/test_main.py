#vamosversesobeostestes
from fastapi.testclient import TestClient
from src.main import app   # ajuste o import caso seu main.py esteja em outra pasta

client = TestClient(app)

def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello, Docker + FastAPI!"}

def test_read_item_without_q():
    resp = client.get("/items/5")
    assert resp.status_code == 200
    assert resp.json() == {"item_id": 5, "q": None}

def test_read_item_with_q():
    resp = client.get("/items/42?q=abc")
    assert resp.status_code == 200
    assert resp.json() == {"item_id": 42, "q": "abc"}
### END
