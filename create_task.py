from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.projects.models import Project
from webapp.task.models import Task
from webapp.user.models import User  
app=create_app()

with app.app_context():
   
    u = Project.query.get(1)
    c=User.query.get(2)
    b=User.query.get(1)
    u.users.append(c)
    db.session.add(u)
    db.session.commit()
    u.users.append(b)
    db.session.add(u)
    db.session.commit()
   
   

