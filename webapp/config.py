import os

SQLALCHEMY_TRACK_MODIFICATIONS = False

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    basedir, "..", "dzen.db"
)

SECRET_KEY = "12321asdwfq!$@123"
SQLALCHEMY_TRACK_MODIFICATIONS = False
render_as_batch=True
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'luzanov.zena@gmail.com'  # введите свой адрес электронной почты здесь
MAIL_DEFAULT_SENDER = 'luzanov.zena@gmail.com'  # и здесь
MAIL_PASSWORD = 'saybrwxfvhvbzpjz'  # введите пароль