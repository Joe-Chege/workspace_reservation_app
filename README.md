# Workspace Reservation App

This is a Flask-based web application for reserving workspaces. It uses SQLAlchemy for database operations, Flask-Admin for administrative interfaces, and Flask-BasicAuth for authentication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- pip
- Virtualenv

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/workspace_reservation_app.git
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set the FLASK_APP environment variable:
    ```bash
    export FLASK_APP=app
    ```
5. Run the application:
    ```bash
    flask run
    ```
6. Alternatively, you can use Gunicorn to run the application:
    ```bash
    gunicorn 'app:create_app()'
    ```

## Usage

Once the server is running, navigate to `http://localhost:5000` in your web browser. You can start reserving workspaces by creating an account and logging in.

## Configuration

The application's configuration is located in `config.py`. You can modify this file to change the application's settings.

In the `create_app` function in `__init__.py`, the application is configured to use basic authentication with the username and password both set to 'admin'. You can change these values to something more secure.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.