from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, login_required, logout_user, current_user
from app.auth.forms import login_form, register_form
from sqlalchemy.orm import load_only
from werkzeug.security import generate_password_hash
from app.db import db
from app.db.models import User
auth = Blueprint('auth', __name__, template_folder='templates')
from flask import current_app

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = login_form()
    if(current_user.is_authenticated):
        return redirect(url_for('auth.dashboard'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.data).first()
        if User is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Welcome','success')
            return redirect(url_for('auth.dashboard'))
    return render_template('login.html', form=form)

@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = register_form()
    return render_template('register.html', form=form)
@auth.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated():
        return redirect(url_for('auth.login'))
