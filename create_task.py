from getpass import getpass
import sys
from datetime import datetime
from webapp import create_app
from webapp.db import db
from webapp.projects.models import Project
from webapp.task.models import Task , Comment
from webapp.user.models import User
app=create_app()

with app.app_context():
    
    date=datetime.now()
    c=User.query.get(1)
    b=Task.query.get(1)
    print(b.comments)
    #new_comment=Comment(text="Example",  date=date, author=c.id, task=b.id)
    #print(new_comment)
    #db.session.add(new_comment)
    #db.session.commit()
   
   
   

