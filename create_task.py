from getpass import getpass
import sys
from datetime import datetime
from webapp import create_app
from webapp.db import db
from webapp.projects.models import Project
from webapp.task.models import Task , Comment, Tag
from webapp.user.models import User
app=create_app()

with app.app_context():
    
   new_user=Tag(name="docs")
   db.session.add(new_user)
   db.session.commit()
   
   
   

