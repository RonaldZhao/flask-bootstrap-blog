from flask_script import Manager, Server

from blog import app
from blog import db
from blog.models import User, Post

__author__ = 'Ronald Zhao'

manager = Manager(app)
manager.add_command('dev', Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)


if __name__ == '__main__':
    manager.run()
