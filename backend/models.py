from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone  
from typing import Optional

# Get the current time in UTC
def utc_now() -> datetime:
    return datetime.now(timezone.utc)

db: SQLAlchemy = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "task"
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    description: Optional[str] = db.Column(db.String(255))
    completed: bool = db.Column(db.Boolean, default=False)
    created_at: datetime = db.Column(db.DateTime(timezone=True), default=utc_now)
    updated_at: datetime = db.Column(db.DateTime(timezone=True), default=utc_now, onupdate=utc_now)
