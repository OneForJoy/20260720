from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "base62-codec"}


def test_encode_endpoint() -> None:
    response = client.post("/encode", json={"input": "hello world", "text": True})
    assert response.status_code == 200
    assert response.json()["base62"] == "AAwf93rvy4aWQVw"


def test_decode_endpoint_text() -> None:
    response = client.post("/decode", json={"input": "AAwf93rvy4aWQVw", "text": True})
    assert response.status_code == 200
    assert response.json()["result"] == "hello world"


def test_decode_endpoint_raw() -> None:
    response = client.post("/decode", json={"input": "AAwf93rvy4aWQVw", "text": False, "raw": True})
    assert response.status_code == 200
    assert response.json()["raw_hex"] == "68656c6c6f20776f726c64"
