from flask import Flask
from .forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initializing application
app = Flask(__name__)



app.config['SECRET_KEY'] = 'a76ee8997a7788e1aec336d50d604b3b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import views