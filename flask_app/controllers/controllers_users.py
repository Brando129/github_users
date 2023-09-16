from flask_app import app
from flask import render_template, redirect, request, session, flash
import requests
from pprint import pprint

# Get Routes
# Route for rendering the Index Page.
@app.get('/')
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

    if response.json()['location'] == None:
        session['location'] = "Not Available"
    else:
        session['location'] = response.json()['location']
    if response.json()['hireable'] == None:
        session['hireable'] = "Not Available"
    else:
        session['hireable'] = response.json()['hireable']
    if response.json()['login'] == None:
        session['login'] = 'Not Available'
    else:
        session['login'] = response.json()['login']
    session['image'] = response.json()['avatar_url']
    if response.json()['name'] == None:
        session['name'] = "Nameless"
    else:
        session['name'] = response.json()['name']
    if response.json()['bio'] == None:
        session['bio'] = 'Not Available'
    else:
        session['bio'] = response.json()['bio']
    if response.json()['blog'] == '':
        session['blog'] = "Not Available"
    else:
        session['blog'] = response.json()['blog']
    if response.json()['public_repos'] == 0:
        session['repos'] = "Not Available"
    else:
        session['repos'] = response.json()['public_repos']
    if response.json()['followers'] == 0:
        session['followers'] = "No Followers"
    else:
        session['followers'] = response.json()['followers']
    if response.json()['company'] == None:
        session['company'] = "Not Available"
    else:
        session['company'] = response.json()['company']
    if response.json()['twitter_username'] == None:
        session['twitter'] = "Not Available"
    else:
        session['twitter'] = response.json()['twitter_username']
    # session['created_at'] = response.json()['created_at']

    return redirect('/user_page')