from app import db
from datetime import datetime

class Prompt(db.Model):
    """
    Model for storing Prompt objects in the database.
    """

    __tablename__ = "prompts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(1255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    metrics = db.Column(db.JSON, nullable=True, default=dict)

    def __repr__(self):
        return f"<Prompt {self.id}>"