from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager,current_user, login_required, login_user, logout_user
from webapp.db import db
from flask_migrate import Migrate
from flask_mail import Mail, Message
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.projects.views import blueprint as projects_blueprint
from webapp.task.views import blueprint as task_blueprint
from webapp.user.models import  User
from webapp.projects.models import Project
from webapp.task.models import Task


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate=Migrate(app,db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(projects_blueprint)
    app.register_blueprint(task_blueprint)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
