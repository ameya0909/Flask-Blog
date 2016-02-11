from flask import render_template
from __init__ import app


@app.route('/')
def hello_world():
    return render_template('index.html', title='Home', user="Ameya")
