

from webapp.db import db

tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
    db.Column("page_id", db.Integer, db.ForeignKey("task.id")),
)
 

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    short_description=db.Column(db.String, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    author = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor = db.Column(db.Integer, db.ForeignKey("user.id"))
    project_id=db.Column(db.Integer, db.ForeignKey("project.id"))
    comments = db.relationship("Comment", backref=db.backref("comment"), lazy=True)
    status = db.Column(db.Integer, db.ForeignKey("status.id"))
    tag = db.relationship(
        "Tag", secondary=tags, backref=db.backref("task_tag"), lazy=True
    )

    @property
    def is_active(self):
        return self.status =='active'
    @property
    def is_wait(self):
        return self.status =='wait'  
    @property 
    def is_disable(self):
        return self.status =='disable'   

    def __repr__(self):
        return f"<Task {self.title} >"


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    task = db.Column(db.Integer, db.ForeignKey("task.id"))

    def __repr__(self):
        return f"<Status {self.name}>"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    attach = db.Column(db.LargeBinary, nullable=True)
    task = db.Column(db.Integer, db.ForeignKey("task.id"))
    author = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Comment {self.text}>"





class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Tag {self.name}>"
