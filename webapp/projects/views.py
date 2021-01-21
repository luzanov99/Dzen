from flask import  Blueprint, render_template, current_app, flash, redirect, url_for
from webapp.projects.models import Project
from webapp.user.models import User
from webapp.projects.forms import ProjectForm, AddUserForm
from webapp.db import db
blueprint=Blueprint('projects', __name__)

@blueprint.route("/")
def index():
    title='Проекты'
    projects_list=Project.query.all()
    return  render_template('projects/index.html', page_title=title, projects_list=projects_list)

@blueprint.route("/<int:id>")
def project_detail(id):
    title='Проект'
    
    project=Project.query.get(id)
    project_tasks=project.tasks.all()
    return  render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)

@blueprint.route("/<int:id>/add_user_to_project")
def add_user_to_project(id):
    project=Project.query.get(id)
    project_form=AddUserForm()
    title='Добавить участника проекта'
    return render_template('projects/add_user_project.html',page_title=title, form=project_form, project=project)

@blueprint.route("/<int:id>/process_add_user_project", methods=['POST'])
def process_add_user_project(id):
    title='Проект'
    project=Project.query.get(id)
    project_tasks=project.tasks.all()
    form = AddUserForm()
    if form.validate_on_submit():
        u = Project.query.get(id)
        user_name=User.query.filter_by(username=form.username.data).first()
        if user_name not in u.users.all():

            u.users.append(user_name)
            db.session.add(u)
            db.session.commit()
            flash("Пользователь успешно добавлен")
        else:
            flash("Такой пользователь уже существует")
            return render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)
        return render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)
    


@blueprint.route("/addproject")
def add_project():
    title='Добавление нового проекта'
    project_form=ProjectForm()
    return render_template('projects/add_project.html',page_title=title, form=project_form)

@blueprint.route('/process_addproject', methods=['POST'])
def process_addproject():
    form = ProjectForm()
    if form.validate_on_submit():
        new_project=Project(name=form.project_name.data)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('projects.index'))
      

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))
