from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone  

# Get the current time in UTC
def utc_now():
    return datetime.now(timezone.utc)

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utc_now)
    updated_at = db.Column(db.DateTime(timezone=True), default=utc_now, onupdate=utc_now)
