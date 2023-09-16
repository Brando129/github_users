from flask_app import app
from flask import render_template, redirect, request, session, flash
import requests
from pprint import pprint

# Get Routes
# Route for rendering the Index Page.
@app.get('/index')
def index_page():
    return render_template('index.html')

# Route for rendering the Users Page
@app.get('/user_page')
def users_page():
    return render_template('user_page.html')

# Post Routes
# Route for searching for a user
@app.post('/search/user_name')
def search_user_name():

    user = request.form['user_name']
    url = f'https://api.github.com/users/{user}'
    response = requests.get(url)

    pprint(response.json())

    session['location'] = response.json()['location']
    session['hireable'] = response.json()['hireable']
    session['login'] = response.json()['login']
    session['image'] = response.json()['avatar_url']
    session['name'] = response.json()['name']
    session['bio'] = response.json()['bio']
    session['blog'] = response.json()['blog']
    session['created_at'] = response.json()['created_at']

    return redirect('/user_page')