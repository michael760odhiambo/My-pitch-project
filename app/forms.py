from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,Label
from wtforms.validators import DataRequired,Email,Length,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('sign Up')

class LoginForm(FlaskForm):
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')    