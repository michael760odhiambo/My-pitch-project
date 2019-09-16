from flask import render_template,url_for,flash,redirect
from .forms import RegistrationForm,LoginForm
from app import app

post = [
    {
        'author':'Michael odhiambo',
        'title':'Pitch 001',
        'content': 'this is his first posted content',
        'date_posted':'April 20, 2019'

    },
    {
        'author':'Grace Kaunda',
        'title': 'Pitch 002',
        'content': 'this is her second posted content',
        'date_posted':'April 21, 2019'

    }
]

@app.route('/')
def home():
    return render_template('index.html',post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {{form.username.data}}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mike@otis.com' and form.password.data == 'michael':
            flash('You have been successfully loged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessfull please check your username and password', 'danger')    
    
    return render_template('login.html',title='login',form=form)    


  