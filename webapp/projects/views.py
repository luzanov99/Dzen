from flask import  Blueprint, render_template, current_app, flash, redirect, url_for
from webapp.projects.models import Project
from webapp.projects.forms import ProjectForm
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
