from fastapi.testclient import TestClient
import sys
sys.path.append('../app/')
from main import app

client = TestClient(app)

def test_user_cant_login_if_it_doesnt_exist():
	response = client.post("/users/signin/", json={"email" : "esteUsuario@NoExiste.com", "password": "MatenmePorFavor"})
	print(response.status_code)
	print(response.json())
	assert response.status_code == 403
	assert response.json() == {"detail": "Incorrect mail or password"}
	
test_user_cant_login_if_it_doesnt_exist()
