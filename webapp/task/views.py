from datetime import datetime
from flask import  Blueprint, render_template, current_app, flash, redirect, url_for, abort
from flask_login import LoginManager,current_user, login_required
from webapp.task.models import Task, Comment, Tag
from webapp.user.models import User
from webapp.task.forms import TaskForm, CommentForm
from webapp.projects.models import Project
from webapp.db import db

blueprint=Blueprint('task', __name__,   url_prefix='/<id_project>/task')



@blueprint.route("/<int:id>")
@login_required
def task_detail(id, id_project):
    project=Project.query.get_or_404(id_project)
    if not current_user.is_admin:
        if current_user in project.users.all():
            user=User
            form=CommentForm()
            
            title='Задача'
            task=Task.query.get_or_404(id)
            comments=task.comments
            return  render_template('task/task_detail.html', page_title=title, task=task, project=project, form=form, comments=comments, user=User)
        else:
            abort(404)
    else:
        user=User
        form=CommentForm()
        project=Project.query.get_or_404(id_project)
        title='Задача'
        task=Task.query.get_or_404(id)
        comments=task.comments
        return  render_template('task/task_detail.html', page_title=title, task=task, project=project, form=form, comments=comments, user=User)


@blueprint.route("/<tag>")
@login_required
def tag_sorted(id_project, tag):
   
    tag_sort=Tag.query.filter(Tag.name==tag).first()
    project=Project.query.get_or_404(id_project)
    title=tag_sort.name
    tasks=tag_sort.task_tag
    return  render_template('task/tag_detail.html', page_title=title, tasks=tasks, project=project )

@blueprint.route("/<int:id>/process_add_comment", methods=['POST'] )
def process_add_comment(id, id_project):
    form = CommentForm()
    
   
    task=Task.query.get_or_404(id)
    project=Project.query.get(id_project)
    comments=task.comments
    if form.validate_on_submit():
        new_comment=Comment(text=form.text.data, date=datetime.now(), task=id, author=current_user.id)
        print("1")
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('task.task_detail', id=task.id, id_project=project.id))
        
    


@blueprint.route("/<int:id>/edit_task")
def edit_task(id, id_project):
    title='Редактирование задачи'
    project=Project.query.get_or_404(id_project)
    task_form=TaskForm()
    task=Task.query.get_or_404(id)
    tags=Tag.query.all()
    groups_list=[(tag.name, tag.name) for tag in tags]
    groups_list_basic=[tag.name for tag in task.tag]
    task_form.tags.choices=groups_list
    task_form.tags.default=groups_list_basic
    task_form.process()
    task_form.title.data=task.title
   
    task_form.description.data=task.description
    task_form.short_description=task.description[0:30]
    
    task_form.due_date.data=task.due_date
    task_form.status.data=task.status
  
    
    
    return  render_template('task/edit_task.html', page_title=title, task=task ,project=project , form=task_form)

@blueprint.route('/<int:id>/process_edittask', methods=['POST'])
def process_edittask(id, id_project):
    project=Project.query.get(id_project)
    form = TaskForm()
    tags=Tag.query.all()
    groups_list=[(tag.name, tag.name) for tag in tags]
    form.tags.choices=groups_list
    if form.validate_on_submit():
        u = Project.query.get_or_404(id_project)
        task_new=Task.query.get_or_404(id)
        task_new.title=form.title.data
        task_new.description=form.description.data
        task_new.short_description=form.description.data[0:30]
        task_new.due_date=form.due_date.data
        task_new.status=form.status.data
        
        db.session.add(task_new)
        db.session.commit()
        for tag in form.tags.data:
            if Tag.query.filter(Tag.name == tag):
                
                tag_task = Tag.query.filter_by(name=tag).first()
                task_new.tag.append(tag_task)
                db.session.add(task_new)
                db.session.commit()
        return redirect(url_for('projects.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))


        return redirect(url_for('task.add_task', id_project=project.id))

@blueprint.route("/add_task")
@login_required
def add_task(id_project):
    project=Project.query.get_or_404(id_project)
    title='Добавление новой задачи'
    task_form=TaskForm()
    tags=Tag.query.all()
    groups_list=[(tag.name, tag.name) for tag in tags]
    task_form.tags.choices=groups_list
    return render_template('task/add_task.html',page_title=title, form=task_form, project=project)

@blueprint.route('/process_addtask', methods=['POST'])
def process_addtask(id_project):
    project=Project.query.get_or_404(id_project)
    tags=Tag.query.all()
    groups_list=[(tag.name, tag.name) for tag in tags]
    form = TaskForm()
   
    form.tags.choices=groups_list
    if form.validate_on_submit():
        u = Project.query.get_or_404(id_project)
        new_task=Task(title=form.title.data,description=form.description.data,project=u, due_date=form.due_date.data, status=form.status.data)
        new_task.short_description=form.description.data[0:30]
        db.session.add(new_task)
        db.session.commit()
        for tag in form.tags.data:
            if Tag.query.filter(Tag.name == tag):
                
                tag_task = Tag.query.filter_by(name=tag).first()
                new_task.tag.append(tag_task)
                db.session.add(new_task)
                db.session.commit()
        
        return redirect(url_for('projects.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))


        return redirect(url_for('task.add_task', id_project=project.id))

    

    