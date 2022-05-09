from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth.decorators import admin_required
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from app.auth.forms import login_form, register_form
from app.db import db
from app.db.models import User
from flask import Blueprint, render_template, request, redirect, url_for, flash

transactions_blueprint = Blueprint('transactions', __name__, template_folder='templates')
from flask import current_app

@transactions_blueprint.route('/transactions')
def transaction():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('transactions.html')