from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField,  FieldList, SelectField, TextAreaField
from wtforms.validators import DataRequired
class TaskForm(FlaskForm):
    title = StringField('Название задачи', validators=[DataRequired()], render_kw={"class": "form-control"})
    description =TextAreaField('Описание задачи', validators=[DataRequired()], render_kw={"class": "form-control"})
    due_date=DateField('Дата публикации', validators=[DataRequired()])
    status=SelectField('Статус',validators=[DataRequired()], choices=[('active', 'Активный'), ('disable', 'Неактивный'), ('wait', 'Ожидание')],render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})


class CommentForm(FlaskForm):
    text=TextAreaField('Добавить комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',  render_kw={"class": "btn btn-primary"})