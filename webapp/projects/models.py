from webapp.db import db
from webapp.task.models import Task

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='project', lazy='dynamic')

    def __repr__(self):
        return f"<Project {self.name}>"
        