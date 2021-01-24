import os

SQLALCHEMY_TRACK_MODIFICATIONS = False

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    basedir, "..", "dzen.db"
)

SECRET_KEY = "12321asdwfq!$@123"
SQLALCHEMY_TRACK_MODIFICATIONS = False
render_as_batch=True