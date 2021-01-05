from flask import  Blueprint, render_template, current_app, flash, redirect, url_for
from webapp.task.models import Task
from webapp.task.forms import TaskForm
blueprint=Blueprint('task', __name__,  url_prefix='/task')

@blueprint.route("/")
def add_task():
    title='Добавление новой задачи'
    project_form=TaskForm()
    return render_template('task/add_task.html',page_title=title, form=project_form)

@blueprint.route("/<int:id>")
def task_detail(id):
    title='Задача'
    task=Task.query.get(id)
    return  render_template('task/task_detail.html', page_title=title, task=task)