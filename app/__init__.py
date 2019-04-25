from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

# Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

# Creating the app configurations
    app.config.from_object(config_options[config_name])

# Registering the blueprint
    from .blogger import blogger as blogger_blueprint
    app.register_blueprint(blogger_blueprint)

    return app