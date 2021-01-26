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
    
    date=datetime.now()
    c=Task.query.get(1)
    
   
    new_tag1=Tag.query.get(1)
    new_tag2=Tag.query.get(2)
    c.tag.append(new_tag1)
    db.session.add(c)
    db.session.commit()
    c.tag.append(new_tag2)
    db.session.add(c)
    db.session.commit()
   
   
   

