from fastapi.testclient import TestClient
import sys
sys.path.append('../app/')
from main import app

client = TestClient(app)

def test():
	response = client.post("/users/signin", json={"email" : "pepito@pepe.com", "password": "pepe"})
	assert response.status_code == 200
	assert response.json() == "Todo OK"
	
test()
