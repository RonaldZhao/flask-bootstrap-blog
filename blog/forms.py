from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

__author__ = 'Ronald Zhao'


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit_btn = SubmitField(label='登录')


class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    user_name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_check = PasswordField(validators=[DataRequired()])
    submit_btn = SubmitField(label='注册')
    # recaptcha = RecaptchaField()


class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    content = TextAreaField(validators=[DataRequired()])
    save_btn = SubmitField(label='保存')


class AlterUserNameForm(FlaskForm):
    new_user_name = StringField(validators=[DataRequired()])
    save_btn = SubmitField(label='保存')
