from app import app, db

from flask import render_template

from app.models import User

@app.route('/')
def index():

    return render_template('base.html')
