# import Flask to create web service
from flask import Flask, render_template
# import sqlite
import sqlite3

# create a new instance of Flask
app = Flask(__name__)

def db_connection():
  # connect to database
  conn = sqlite3.connect('bookstore.db')
  # allows us to access the columns of the database by name like a Python dictionary
  conn.row_factory = sqlite3.Row
  # access the database using a cursor object
  return conn

# use a route decorator to create a route for the homepage
@app.route('/')
# create a function that will return the data from the database
def index():
  # opens the database connection
  conn = db_connection()
  # fetches all the data from the top_books table
  data = conn.execute('''SELECT * FROM top_books''').fetchall()
  # closes database connection
  conn.close()
  # returns data to the user
  return render_template('index.html', data=data)

# debug mode means that the server will reload itself on code changes
if __name__ == '__main__':
  app.run(debug=True)