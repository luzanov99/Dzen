from flask_mail import Mail, Message
from webapp import create_app
app=create_app()
mail = Mail(app)
with app.app_context():
    msg = Message("Subject", recipients=['luzanov.zena@gmail.com'])
    msg.body = "Mail body"
    mail.send(msg)