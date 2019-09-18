from flask import Flask
from .config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_bootstrap import Bootstrap
import secrets

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'




db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

        # configure UploadSet
    configure_uploads(app,photos)

    # Creating the app configurations
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing flask extensions
    
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    # setting config
    app.config['SECRET_KEY']= '73a5487ab8399681a1dbef1a8f054029'
    




    return app