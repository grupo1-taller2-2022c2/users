from fastapi.testclient import TestClient
import sys
sys.path.append('../app')
from main import app

client = TestClient(app)

def test():
	assert(True)

test()
