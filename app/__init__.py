from flask import Flask
from .forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy

# Initializing application
app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'a76ee8997a7788e1aec336d50d604b3b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:mike1234@localhost/lights'

from app import views