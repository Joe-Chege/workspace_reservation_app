# app/rooms/routes.py

from flask import Blueprint, render_template

rooms_blueprint = Blueprint('rooms', __name__)

@rooms_blueprint.route('/')
def index():
    return render_template('rooms/index.html')
