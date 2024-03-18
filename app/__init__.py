# app/__init__.py
from flask import Flask
from flask_login import LoginManager
from .extensions import db, migrate
from .models.user import User
from .config import Config  # Add this line

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Config is now defined

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Set up Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # Define the user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app