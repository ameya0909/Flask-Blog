from flask import render_template
from __init__ import app
from forms import LoginForm


@app.route('/')
def hello_world():
    return render_template('index.html', title='Home', user="Ameya")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='Login')
