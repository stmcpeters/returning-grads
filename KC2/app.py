# import Flask to create web service
from flask import Flask, render_template, url_for, redirect, session, request
# import sqlite
import sqlite3
# import dotenv and os module to access environment variables
from dotenv import load_dotenv
import os
# import OAuth from authlib to authenticate users
from authlib.integrations.flask_client import OAuth

# load environment variables from .env file
# assign the environment variables to variables to be used
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
SITE_KEY = os.getenv('SITE_KEY')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# create a new instance of Flask
app = Flask(__name__)
app.secret_key = SECRET_KEY

# OAuth config
oauth = OAuth(app)
# create a new instance of OAuth
google = oauth.register(
  name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'email profile'},
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
)

def db_connection():
  # connect to database
  connection = sqlite3.connect('bookstore.db')
  # allows us to access the columns of the database by name like a Python dictionary
  connection.row_factory = sqlite3.Row
  # access the database using a cursor object
  return connection

# use a route decorator to create a route for the landing page to prompt CAPTCHA and sign in with google button
@app.route('/')
def landing():
  return render_template('home.html', site_key=SITE_KEY)

# use a route decorator to create a route for the page showing the data
@app.route('/data')
# create a function that will return the data from the database
def index():
  # opens the database connection
  connection = db_connection()
  # fetches all the data from the top_books table
  data = connection.execute('''SELECT * FROM top_books''').fetchall()
  # closes database connection
  connection.close()
  # returns data to the user
  return render_template('index.html', data=data)

# use a route decorator to create a route redirecting to the google login page
@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

# use a route decorator to create a route for redirecting after successful login
@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = oauth.google.authorize_access_token()
    resp = oauth.google.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    # will redirect to the data page after successful login
    return redirect('/data')

# debug mode means that the server will reload itself on code changes
if __name__ == '__main__':
  app.run(debug=True)