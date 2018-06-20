import datetime

from flask import render_template, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
import markdown

from blog import app, db
from blog.models import User, Post
from blog.forms import LoginForm, RegisterForm, PostForm, AlterUserNameForm

__author__ = 'Ronald Zhao'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@app.route('/index')
def index():
    year = datetime.datetime.now().year
    posts = Post.query.order_by(Post.post_time.desc()).all()
    return render_template('index.html', pathname='index', year=year, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # 如果已经登录则直接跳转到首页
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('此用户不存在！')
        elif check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('密码错误！')
    return render_template('login_or_register.html', pathname='login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  # 如果已经登录则直接跳转到首页
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:  # 如果已经注册
            flash('此邮箱已经注册！')
        elif form.password.data != form.password_check.data:
            flash('两次密码输入不一致！')
        else:
            user = User(form.user_name.data, form.email.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('注册成功！')
            return redirect(url_for('login'))
    return render_template('login_or_register.html', pathname='register', form=form)


@app.route('/logout')
def logout():
    if not current_user.is_authenticated:
        flash('请先登录')
        return redirect(url_for('login'))
    logout_user()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html', pathname='about')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', pathname='timeline')


def markdown2html(md):
    html = markdown.markdown(md)
    pass


@app.route('/post', methods=['GET', 'POST'])
def post():
    if not current_user.is_authenticated:  # 如果未登录则重定向到登录页
        flash('请先登录！')
        return redirect(url_for('login'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data)
        post.author = current_user
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html', pathname='post', form=form)


@app.route('/userinfo')
def userinfo():
    if not current_user.is_authenticated:  # 如果未登录则重定向到登录页
        flash('请先登录！')
        return redirect(url_for('login'))
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('userinfo.html', pathname='userinfo', posts=posts, form=AlterUserNameForm())


@app.route('/detail/<int:id>')
def detail(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('没有这篇文章，登录进行写作吧~')
        return redirect(url_for('login'))
    return render_template('detail.html', pathname='detail', post=post)


@app.route('/editpost/<int:id>')
def editpost(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('没有这篇文章，登录进行写作吧~')
        return redirect(url_for('login'))
    elif not current_user.is_authenticated:
        flash('需要登录才能修改！')
        return redirect(url_for('login'))
    elif current_user.email != post.author.email:
        return redirect(url_for('index'))
    return render_template('editpost.html', post=post, pathname='post')


@app.route('/alterusername', methods=['GET', 'POST'])
def alterusername():
    if current_user.is_authenticated:
        form = AlterUserNameForm()
        current_user.user_name = form.new_user_name.data
        db.session.commit()
        flash('修改成功！')
        return redirect(url_for('userinfo'))
    flash('请登录！')
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
