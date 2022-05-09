import csv
import os
from os.path import join, dirname, realpath

from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename

from app.auth.decorators import admin_required
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from app.auth.forms import login_form, register_form
from app.db import db
from app.db.models import User, Transactions
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.transactions.forms import csv_upload

transactions_blueprint = Blueprint('transactions', __name__, template_folder='templates')
from flask import current_app

@transactions_blueprint.route('/transactions')
def transaction():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('transactions.html')

@transactions_blueprint.route('/transactions/upload', methods=['POST', 'GET'])
def upload():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    form = csv_upload()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        transactions = []
        with open(filepath, encoding='utf-8-sig') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                transactions.append(Transactions(row['AMOUNT'], row['TYPE']))
        current_user.transactions = transactions + current_user.transactions
        db.session.commit()
        return redirect(url_for('transactions.transaction'))
    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)

