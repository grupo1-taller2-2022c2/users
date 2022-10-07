from fastapi.testclient import TestClient

# Invertir el descomentado al pushear
# from app.main import app
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.json() == {"message": "Go sign in"}


test_root()
