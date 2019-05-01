from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

simple = SimpleMDE()
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)

# Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    mail.init_app(app)

# Creating the app configurations
    app.config.from_object(config_options[config_name])

# configure UploadSet
    configure_uploads(app,photos)

# Registering the blueprint
    from .myblog import myblog as myblog_blueprint
    app.register_blueprint(myblog_blueprint,url_prefix = '/')
    
    from .blogger import blogger as blogger_blueprint
    app.register_blueprint(blogger_blueprint,url_prefix = '/blog')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app