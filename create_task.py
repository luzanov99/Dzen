from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.projects.models import Project
from webapp.task.models import Task
app=create_app()

with app.app_context():
    project_name=input('Введите название проекта')
    new_project=Project(name= project_name)
    db.session.add(new_project)
    db.session.commit()
    u = Project.query.get(1)
    task_name=input('Введите название задачи')
    new_task=Task(title=task_name, project=u)
    db.session.add(new_task)
    db.session.commit()
    task_name=input('Введите название задачи')
    new_task=Task(title=task_name, project=u)
    db.session.add(new_task)
    db.session.commit()
    task_name=input('Введите название задачи')
    new_task=Task(title=task_name, project=u)
    db.session.add(new_task)
    db.session.commit()


