# app/bookings/routes.py
from flask import Blueprint, render_template

bookings_blueprint = Blueprint('bookings', __name__)

@bookings_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    # Your code for creating a booking goes here
    return render_template('bookings/create.html')