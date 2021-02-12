from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import db
from webapp.task.models import Comment


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    userpic_url = db.Column(db.String(), nullable=True)
    comments = db.relationship("Comment", backref=db.backref("comments"), lazy=True)
    messages = db.relationship("Messege", backref=db.backref("messege"), lazy=True)
    role =db.Column(db.String(10), index=True)
    
    def set_password(self, password):
        self.password=generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role =='admin'

    def __repr__(self):
        return f"<User {self.username}>"


class Messege(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text=db.Column(db.Text, nullable=True)
    status=db.Column(db.String(), nullable=True)
    project_id=db.Column(db.Integer, nullable=True)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))

    
    
    