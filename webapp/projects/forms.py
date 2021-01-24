from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    project_name = StringField('Название проекта', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})


class AddUserForm(FlaskForm):
    username=StringField('Имя пользователя',validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})

class MessegeForm(FlaskForm):
    text=StringField('Сообщение для администратора', validators=[DataRequired()], render_kw={"class": "form-control"})
    status=SelectField('Тип запроса ',validators=[DataRequired()], choices=[('access', 'Запрос доступа'), ('violation', 'Нарушение правил'), ('another', 'Другая причина')],render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})