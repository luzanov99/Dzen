from flask_login import LoginManager,current_user, login_required, login_user, logout_user
from flask import  Blueprint, render_template, current_app, flash, redirect, url_for, abort
from webapp.projects.models import Project, ChatMessages
from webapp.user.models import User, Messege
from flask_mail import Mail, Message

from webapp.projects.forms import ProjectForm, AddUserForm, MessegeForm
from webapp.db import db
blueprint=Blueprint('projects', __name__)



@blueprint.route("/")
def index():
    if current_user.is_authenticated:
        title='Проекты'
        projects_list=Project.query.all()
        return  render_template('projects/index.html', page_title=title, projects_list=projects_list)
    else :
        return redirect(url_for('user.login'))

@blueprint.route("/<int:id>")
@login_required
def project_detail(id):
    title='Проект'
    
    project=Project.query.get_or_404(id)
    if current_user.is_admin:
        
        project_tasks=project.tasks.all()
        return  render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)
    else:
        if current_user in project.users.all():
            project_tasks=project.tasks.all()
            return  render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)
        else: 
            abort(404)




@blueprint.route("/<int:id>/send_messege")
@login_required
def send_messege(id):
    project=Project.query.get_or_404(id)
    messege_form=MessegeForm()
    title='Запрос к администратору'
    return render_template('projects/send_messege.html',page_title=title, form=messege_form, project=project)

@blueprint.route("/<int:id>/process_send_messege",  methods=['POST'])
def process_send_messege(id):
    project=Project.query.get_or_404(id)
    form = MessegeForm()
    mail = Mail(current_app)
   

    if form.validate_on_submit():
        new_messege=Messege(text=form.text.data,user_id=current_user.id, status=form.status.data, project_id=project.id)
        db.session.add(new_messege)
        db.session.commit()
        with current_app.app_context():
            msg = Message("Subject", recipients=['luzanov.zena@gmail.com'])
            msg.body = form.text.data
            mail.send(msg)
        return redirect(url_for('projects.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))


        return redirect(url_for('task.send_messege', id=project.id))

    

@blueprint.route("/<int:id>/add_user_to_project")
@login_required
def add_user_to_project(id):
    project=Project.query.get_or_404(id)
    project_form=AddUserForm()
    title='Добавить участника проекта'
    return render_template('projects/add_user_project.html',page_title=title, form=project_form, project=project)

@blueprint.route("/<int:id>/process_add_user_project", methods=['POST'])
def process_add_user_project(id):
    title='Проект'
    project=Project.query.get_or_404(id)
    project_tasks=project.tasks.all()
    form = AddUserForm()
    if form.validate_on_submit():
        u = Project.query.get_or_404(id)
        user_name=User.query.filter_by(username=form.username.data).first()
        if user_name !=None:
            if user_name not in u.users.all():

                u.users.append(user_name)
                db.session.add(u)
                db.session.commit()
                flash("Пользователь успешно добавлен")
            else:
                flash("Такой пользователь уже существует")
                return render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)
        else:
            flash("Такого пользователя нет")
            return redirect(url_for('projects.add_user_to_project', id=project.id))
        return render_template('projects/post_detail.html', page_title=title, project=project, project_tasks=project_tasks)
    


@blueprint.route("/addproject")
@login_required
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

@blueprint.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404