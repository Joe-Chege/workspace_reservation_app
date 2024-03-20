# app/main/routes.py
from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('main/index.html')  # Update the path to 'main/index.html'

@main_bp.route('/protected')
@login_required
def protected():
    return render_template('main/protected.html')  # Update the path to 'main/protected.html'
