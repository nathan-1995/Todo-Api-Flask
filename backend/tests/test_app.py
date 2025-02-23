import pytest
from typing import Any, Dict, Generator, List
from flask.testing import FlaskClient
from backend.app import app, db
from backend.models import Task

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    """
    Creates a fresh database and a test client before each test,
    then tears down afterward.
    """
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()

# Test the post endpoint
def test_create_task(client: FlaskClient) -> None:
    resp = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Test Description"
    })
    assert resp.status_code == 201
    json_data: Dict[str, Any] = resp.get_json()
    assert json_data["message"] == "Task created successfully."

# Test the get endpoint
def test_get_tasks(client: FlaskClient) -> None:
    # Create two tasks
    client.post("/tasks", json={"title": "Task One", "description": "First task"})
    client.post("/tasks", json={"title": "Task Two", "description": "Second task"})
    resp = client.get("/tasks") # 
    tasks: List[Dict[str, Any]] = resp.get_json() # Get the JSON data from the response
    assert isinstance(tasks, list)
    assert len(tasks) == 2
    # Tasks are ordered by creation date, so the first task should be "Task Two"
    assert tasks[0]["title"] == "Task Two"
    assert tasks[0]["completed"] is False 

# Test the put endpoint
def test_mark_task_as_completed(client: FlaskClient) -> None:
    client.post("/tasks", json={"title": "Task to Complete", "description": "Needs to be completed"})
    tasks: List[Dict[str, Any]] = client.get("/tasks").get_json()
    assert tasks, "No tasks found to update"
    task_id: int = tasks[0]["id"]
    resp = client.put(f"/tasks/{task_id}", json={"completed": True})
    assert resp.status_code == 200
    updated_tasks: List[Dict[str, Any]] = client.get("/tasks").get_json()
    assert len(updated_tasks) == 0
