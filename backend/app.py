from flask import Flask, request, jsonify, abort, Response
from flask_cors import CORS
from backend.config import Config
from backend.models import db, Task
from typing import Any, Dict, Tuple, List
import logging

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger: logging.Logger = logging.getLogger(__name__)

# Create Flask application
app: Flask = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Init the database
db.init_app(app)
with app.app_context():
    db.create_all()
    logger.info("Database tables created")

# Endpoint for creating a new task
@app.route("/tasks", methods=["POST"])
def create_task() -> Tuple[Response, int]:
    data: Dict[str, Any] = request.get_json()
    if not data or "title" not in data:
        logger.error("Missing required fields in request data: %s", data)
        return jsonify({"error": "Missing required fields"}), 400
    new_task: Task = Task(
        title=data["title"],
        description=data.get("description", "")
    )
    db.session.add(new_task)
    db.session.commit()
    logger.info("Created task with title: %s", new_task.title)
    return jsonify({"message": "Task created successfully."}), 201

# Endpoint for getting the newest 5 tasks
@app.route("/tasks", methods=["GET"])
def get_tasks() -> Tuple[Response, int]:
    tasks: List[Task] = Task.query\
        .filter_by(completed=False)\
        .order_by(Task.created_at.desc())\
        .limit(5)\
        .all()
    
    # Convert the tasks to JSON
    result: List[Dict[str, Any]] = [{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at.isoformat() if task.created_at else None
    } for task in tasks]
    
    logger.debug("Fetched %d tasks", len(result))
    return jsonify(result), 200

# Endpoint for marking a task as completed
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def mark_task_as_completed(task_id: int) -> Tuple[Response, int]:
    # Get the task by ID
    task: Task = db.session.get(Task, task_id)
    if task is None:
        logger.error("Task with id %d not found", task_id)
        abort(404)
    data: Dict[str, Any] = request.get_json()
    task.completed = data.get("completed", True)
    db.session.commit()
    logger.info("Marked task id %d as completed", task_id)
    return jsonify({"message": "Task updated successfully."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)