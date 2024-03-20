from flask import Flask
from flask_login import LoginManager
from .extensions import db, migrate
from .models.user import User
from .config import Config
from .main.routes import main_bp
from .bookings.routes import bookings_blueprint
from .rooms.routes import rooms_blueprint
from .resources.routes import resources_blueprint
from .auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

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
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(bookings_blueprint)
    app.register_blueprint(rooms_blueprint)
    app.register_blueprint(resources_blueprint)

    return app
