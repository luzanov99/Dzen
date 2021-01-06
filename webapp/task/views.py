from flask import  Blueprint, render_template, current_app, flash, redirect, url_for
from webapp.task.models import Task
from webapp.task.forms import TaskForm
from webapp.projects.models import Project
from webapp.db import db
blueprint=Blueprint('task', __name__,   url_prefix='/<id_project>/task')



@blueprint.route("/<int:id>")
def task_detail(id, id_project):
    title='Задача'
    task=Task.query.get(id)
    return  render_template('task/task_detail.html', page_title=title, task=task)

@blueprint.route("/add_task")
def add_task(id_project):
    project=Project.query.get(id_project)
    
    title='Добавление новой задачи'
    project_form=TaskForm()
    return render_template('task/add_task.html',page_title=title, form=project_form, project=project)

@blueprint.route('/process_addtask', methods=['POST'])
def process_addtask(id_project):
    
    form = TaskForm()
    #if form.validate_on_submit():
    u = Project.query.get(id_project)
    new_task=Task(title=form.title.data,description=form.description.data,project=u, due_date=form.due_date.data)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('projects.index'))
    

    