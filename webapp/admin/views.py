from webapp.user.decorators import admin_required
from flask import  Blueprint, render_template
from webapp.user.models import Messege, User
from webapp.projects.models import Project

blueprint=Blueprint('admin', __name__, url_prefix='/admin')
@blueprint.route('/')
@admin_required
def admin_index():
    messeges_list=Messege.query.all()
    users= User
    projects=Project
    title="Панель управления"
    return render_template('admin/index.html', page_title=title, messeges_list=messeges_list, users=users, projects=projects)
