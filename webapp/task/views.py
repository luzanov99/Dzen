from flask import  Blueprint, render_template, current_app, flash, redirect, url_for
from webapp.task.models import Task
from webapp.task.forms import TaskForm
from webapp.projects.models import Project
from webapp.db import db
blueprint=Blueprint('task', __name__,   url_prefix='/<id_project>/task')



@blueprint.route("/<int:id>")
def task_detail(id, id_project):
    project=Project.query.get(id_project)
    title='Задача'
    task=Task.query.get(id)
    return  render_template('task/task_detail.html', page_title=title, task=task, project=project )

@blueprint.route("/<int:id>/edit_task")
def edit_task(id, id_project):
    title='Редактирование задачи'
    project=Project.query.get(id_project)
    task_form=TaskForm()
    task=Task.query.get(id)
    task_form.title.data=task.title
    task_form.description.data=task.description
    task_form.due_date.data=task.due_date
    task_form.status.data=task.status
    return  render_template('task/edit_task.html', page_title=title, task=task ,project=project , form=task_form)

@blueprint.route('/<int:id>/process_edittask', methods=['POST'])
def process_edittask(id, id_project):
    project=Project.query.get(id_project)
    form = TaskForm()
    if form.validate_on_submit():
        u = Project.query.get(id_project)
        task_new=Task.query.get(id)
        task_new.title=form.title.data
        task_new.description=form.description.data
        task_new.due_date=form.due_date.data
        task_new.status=form.status.data
        db.session.add(task_new)
        db.session.commit()
        return redirect(url_for('projects.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))


        return redirect(url_for('task.add_task', id_project=project.id))

@blueprint.route("/add_task")
def add_task(id_project):
    project=Project.query.get(id_project)
    title='Добавление новой задачи'
    task_form=TaskForm()
    return render_template('task/add_task.html',page_title=title, form=task_form, project=project)

@blueprint.route('/process_addtask', methods=['POST'])
def process_addtask(id_project):
    project=Project.query.get(id_project)
    form = TaskForm()
    if form.validate_on_submit():
        u = Project.query.get(id_project)
        new_task=Task(title=form.title.data,description=form.description.data,project=u, due_date=form.due_date.data, status=form.status.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('projects.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))


        return redirect(url_for('task.add_task', id_project=project.id))

    

    