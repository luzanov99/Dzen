from flask import  Blueprint, render_template, current_app
from webapp.projects.models import Project
blueprint=Blueprint('projects', __name__)

@blueprint.route("/")
def index():
    title='Проекты'
    projects_list=Project.query.all()
    return  render_template('projects/index.html', page_title=title, projects_list=projects_list)

