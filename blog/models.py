from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from sqlalchemy import text

from blog import db

__author__ = 'Ronald Zhao'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self._user_name


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    post_time = db.Column(db.TIMESTAMP(True), server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.title
