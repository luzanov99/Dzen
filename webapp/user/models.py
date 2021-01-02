from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(50), unique=True, index=True, nullable=False
    )
    password = db.Column(db.String(128), nullable=False)
    userpic_url = db.Column(db.String(), nullable=True)
    comment = db.relationship("Comment", backref=db.backref("user"), lazy=True)
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