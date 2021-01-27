from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField,  FieldList, SelectField, TextAreaField, DecimalField, SelectMultipleField
from wtforms.validators import DataRequired
from webapp.task.models import Tag



class TaskForm(FlaskForm):
    
    title = StringField('Название задачи', validators=[DataRequired()], render_kw={"class": "form-control"})
    description =TextAreaField('Описание задачи', validators=[DataRequired()], render_kw={"class": "form-control"})
    due_date=DateField('Дата публикации', validators=[DataRequired()])
    status=SelectField('Статус',validators=[DataRequired()], choices=[('active', 'Активный'), ('disable', 'Неактивный'), ('wait', 'Ожидание')],render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})
    tags=  SelectMultipleField('Теги',  render_kw={"class": "chosen-select"}, coerce=str)

class CommentForm(FlaskForm):
    text=TextAreaField('Добавить комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})