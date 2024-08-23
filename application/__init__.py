from . import serial
from flask import Flask


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    serial.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
    
        return app
