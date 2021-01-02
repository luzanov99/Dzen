from flask_login import LoginManager,current_user, login_required, login_user, logout_user
from flask import  Blueprint, Flask, render_template, flash, redirect, url_for
from webapp.user.forms import LoginForm
from webapp.user.models import  User


blueprint=Blueprint('user', __name__, url_prefix='/users')
@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('projects.index'))
    title="Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('projects.index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')

def logout():
    logout_user()
    flash("Выуспешно разлогинились")
    return redirect(url_for('projects.index'))