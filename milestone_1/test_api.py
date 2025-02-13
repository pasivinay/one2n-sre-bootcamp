import pytest
from app import app, db
from models import Student

@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_healthcheck(test_client):
    response = test_client.get('/api/v1/healthcheck/')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_add_student(test_client):
    response = test_client.post('/api/v1/students', json={"name": "John Doe", "age": 25})
    assert response.status_code == 201
    assert response.json["name"] == "John Doe"
    assert response.json["age"] == 25

def test_get_students(test_client):
    response = test_client.get('/api/v1/students/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_student(test_client):
    with app.app_context():
        student = db.session.get(Student, 1)
    
    response = test_client.get('/api/v1/students/1/')
    assert response.status_code == 200
    assert response.json["name"] == student.name

def test_update_student(test_client):
    response = test_client.put('/api/v1/students/1/', json={"name": "Jane Doe", "age": 26})
    assert response.status_code == 200
    assert response.json["name"] == "Jane Doe"
    assert response.json["age"] == 26

def test_delete_student(test_client):
    response = test_client.delete('/api/v1/students/1/')
    assert response.status_code == 200
    assert response.json == {"message": "Student deleted"}

def test_get_student_not_found(test_client):
    response = test_client.get('/api/v1/students/99/')
    assert response.status_code == 404
    assert response.json == {"message": "Student not found"}
