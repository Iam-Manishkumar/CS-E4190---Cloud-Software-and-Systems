from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_course():
    response = client.get('/courses/CS-E4190')
    assert response.json() == {"id": "CS-E4190", "name": "Cloud software and systems",
                 "instructor": "Mario Di francesco", "keyword": ["cloud", "container"]}
    assert response.status_code == 200


def test_read_nonexistent_course():
    response = client.get('/courses/ComputerScience-E202828')
    assert response.json() == {"detail": "Course does not exist"}
    assert response.status_code == 404


def test_create_course():
    response = client.post('/courses/',json={"id": "CloudComputing-2028", "name": "CloudComputing",
                 "instructor": "Manish", "keyword": ["cloud", "docker"]})
    assert response.json() == {"id": "CloudComputing-2028", "name": "CloudComputing",
                 "instructor": "Manish", "keyword": ["cloud", "docker"]}
    assert response.status_code == 200

def test_create_existing_course():
    response = client.post('/courses/',json={"id": "CS-E4190", "name": "Cloud software and systems",
                 "instructor": "Mario Di francesco", "keyword": ["cloud", "container"]})
    assert response.json() == {"detail": "Course already exists"}
    assert response.status_code == 400