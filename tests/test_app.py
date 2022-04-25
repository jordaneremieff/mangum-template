from pathlib import Path

from fastapi.testclient import TestClient

from src.app import app, conf


SRC_PATH = Path(__file__).resolve().parent.parent / "src"


def test_get_lambda_info():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    response_json = response.json()
    assert set(response_json["dependencies"]) == {
        i.name for i in conf.LIB_PATH.iterdir()
    }
    assert response_json["event"] == {}
