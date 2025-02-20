from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# create connection to database tech_news.db
def news_db_connection():
    # connect to database
    connection = sqlite3.connect('tech_news.db')
    # allows us to access the columns of the database by name like a Python dictionary
    connection.row_factory = sqlite3.Row
    # access the database using a cursor object
    return connection

# create connection to database jokes_api.db
def jokes_db_connection():
    # connect to database
    conn = sqlite3.connect('jokes_api.db')
    # allows us to access the columns of the database by name like a Python dictionary
    conn.row_factory = sqlite3.Row
    # access the database using a cursor object
    return conn


@app.route('/', methods=['GET'])
def index():
    # opens connection to database
    connection = news_db_connection()
    conn = jokes_db_connection()
    # fetch data from articles table
    data = connection.execute('''SELECT * FROM articles''').fetchall()
    joke = conn.execute('''SELECT * FROM tech_jokes LIMIT 1''').fetchone()
    # close database connection
    connection.close()
    conn.close()
    # render articles data in index.html and pass data in order to display
    return render_template('index.html', data=data, joke=joke)

@app.route('/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        # opens the database connection
        connection = news_db_connection()
        # form data from the user
        title = request.form['title']
        description = request.form['description']
        link = request.form['article_link']
        # adds the data to the articles table 
        connection.execute('''INSERT INTO articles (title, description, article_link) VALUES (?, ?, ?)''', (title, description, link))
        # saves the changes
        connection.commit()
        # closes database connection
        connection.close()
        # redirects to the index.html page
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_article(id):
    # open connection to database 
    connection = news_db_connection()
    if request.method == "POST":
      # form data from user
      title = request.form['title']
      description = request.form['description']
      link = request.form['article_link']
      # updates data from specified id in the articles table
      connection.execute('''UPDATE articles SET title = ?, description = ?, article_link = ? WHERE id = ?''', (title, description, link, id))
      # commit the changes
      connection.commit()
      # close database connection
      connection.close()
      # redirect to home page
      return redirect(url_for('index'))
    else:
      # will populate the article's info to be edited in the form
      article = connection.execute('''SELECT * FROM articles WHERE id = ?''', (id,)).fetchone()
      # close the connection to database
      connection.close()
      # will render the edit.html template with article info
      return render_template('edit.html', article=article)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_article(id):
    # open connection to database
    connection = news_db_connection()
    # query to delete specified id from the articles table
    article = connection.execute('''DELETE FROM articles WHERE id = ?''',(id,))
    # commit the changes 
    connection.commit()
    # close the database connection
    connection.close()
    # render deletion template to confirm article was deleted
    return render_template('delete.html', article=article)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)