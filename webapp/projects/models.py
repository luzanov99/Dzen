from webapp.db import db
from webapp.task.models import Task
from webapp.user.models import User
users_on_projets = db.Table("users_on_projets",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("project_id", db.Integer, db.ForeignKey("project.id")),
)
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='project', lazy='dynamic')
    users=db.relationship('User',secondary=users_on_projets, backref='user_project', lazy='dynamic')
    def __repr__(self):
        return f"<Project {self.name}>"
class ChatMessages(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256))
    msg      = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.username
        