# import Flask to create web service
from flask import Flask, render_template, render_template_string, url_for, redirect, request
# import login-required decorator from flask_login
from flask_login import login_required
# import flask limiter for rate limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
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

# flask-limiter config
limiter = Limiter(
  # use the user's IP address for rate limiting
    get_remote_address, 
    app=app,
    # sets a global rate limit (e.g., 15 requests per hour)
    default_limits=["15 per hour"], 
)

# error handling for exceeding rate limit
@app.errorhandler(429)
def ratelimit_error(e):
    # allows you to render a template from a string
    return render_template_string('''
        <html>
        <head>
            <script type="text/javascript">
                alert("You have exceeded your request limit! Please try again later.");
                window.history.back();  // returns to landing page
            </script>
        </head>
        <body></body>
        </html>
    '''), 429

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
@limiter.limit("5 per minute") # limits to 5 req/min
def landing():
  return render_template('home.html', site_key=SITE_KEY)

# use a route decorator to create a route for the page showing the data
# login_required makes sure user auth is successful before showing data
@login_required
@app.route('/data')
@limiter.limit("5 per minute") # limits to 5 req/min
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
@limiter.limit("5 per minute") # limits to 5 req/min
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

# use a route decorator to create a route for redirecting after successful login
@app.route('/authorize')
@limiter.limit("5 per minute") # limits to 5 req/min
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