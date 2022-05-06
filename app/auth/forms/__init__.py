from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class login_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.data_required
    ])
    password = PasswordField('Password', [
        validators.data_required,
        validators.length(min=6,max=16)
    ])
    submit = SubmitField()

class register_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.data_required
    ])
    password = PasswordField('Password', [
        validators.data_required,
        validators.length(min=6,max=16),
        validators.EqualTo('confirm', message="Passwords must match!")
    ], description="Create a password")
    confirm = PasswordField('Repeat Password', description="Please confirm that passwords match!")
    submit = SubmitField()



