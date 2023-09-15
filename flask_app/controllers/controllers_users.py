from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import models_user

# Get Routes
@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/users_page')
def users_page():
    return render_template('users_page.html')

# Post Routes
