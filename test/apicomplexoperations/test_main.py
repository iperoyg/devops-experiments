from apicomplexoperations.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


class TestFastAPIMain:

    def test_root_get(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_math_get(self):
        response = client.get("/math/0")
        assert response.status_code == 200
        assert response.json() == {"message": 1}

    def test_string_get(self):
        response = client.get("/string?text=abc&number=2")
        assert response.status_code == 200
        assert response.json() == {"message": "bac"}

    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"message": "Healthy"}
