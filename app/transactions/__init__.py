from flask import Blueprint, render_template, request, redirect, url_for, flash

transactions = Blueprint('transactions', __name__, template_folder='templates')
from flask import current_app

@transactions.route('/transactions')
def transactions():
    return render_template()