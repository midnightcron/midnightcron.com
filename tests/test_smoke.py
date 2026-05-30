from fastapi.testclient import TestClient

from app.main import app
from app.projects import PROJECTS

client = TestClient(app)


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_landing_renders_with_all_projects() -> None:
    response = client.get("/")
    assert response.status_code == 200
    for project in PROJECTS:
        assert project["name"] in response.text


def test_about_renders() -> None:
    response = client.get("/about")
    assert response.status_code == 200
    assert "Robin Worreby" in response.text


def test_project_detail_renders() -> None:
    response = client.get("/projects/badi-monitor")
    assert response.status_code == 200
    assert "Badi Monitor" in response.text
    assert "TimescaleDB" in response.text


def test_unknown_project_returns_404() -> None:
    assert client.get("/projects/does-not-exist").status_code == 404
