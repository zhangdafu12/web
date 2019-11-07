# -*- encoding:utf8 -*-
# author: Shulei
# e-mail: 1191543592@qq.com
# time:  2019/4/2 19:52
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class LoginForm(FlaskForm):
    account = StringField()
    password = StringField()


class RegistForm(FlaskForm):
    account = StringField()
    nick_name = StringField()
    password1 = StringField()
    password2 = StringField()

