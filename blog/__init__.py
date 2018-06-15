import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

__author__ = 'Ronald Zhao'

app = Flask(__name__)
Markdown(app)
app.secret_key = os.urandom(20)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from blog import views
