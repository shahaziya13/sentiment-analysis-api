from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_single_sentiment():
    response = client.post(
        "/api/analyze",
        json={"text": "I absolutely loved this movie!"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "sentiment" in data
    assert "confidence" in data
    assert "scores" in data

    assert data["sentiment"] in ["positive", "negative", "neutral"]


def test_batch_sentiment():
    response = client.post(
        "/api/analyze/batch",
        json={
            "texts": [
                "I loved this!",
                "This was terrible.",
                "The movie was released yesterday."
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "results" in data
    assert len(data["results"]) == 3


def test_empty_text():
    response = client.post(
        "/api/analyze",
        json={"text": ""}
    )

    assert response.status_code == 422


def test_batch_limit():
    response = client.post(
        "/api/analyze/batch",
        json={
            "texts": ["test"] * 11
        }
    )

    assert response.status_code == 422