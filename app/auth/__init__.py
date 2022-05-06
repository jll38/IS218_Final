from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, login_required, logout_user, current_user
from app.auth.forms import login_form, register_form

auth = Blueprint('auth', __name__, template_folder='templates')
from flask import current_app

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = login_form()
    return render_template('login.html', form=form)

@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = register_form()
    return render_template('register.html', form=form)