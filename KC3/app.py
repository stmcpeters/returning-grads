# import flask and render_template
from flask import Flask, request, render_template, redirect, url_for
# import sqlite
import sqlite3

# create a connection to the database
app = Flask(__name__)

def db_connection():
    # connect to database
    connection = sqlite3.connect('bookstore.db')
    # allows us to access the columns of the database by name like a Python dictionary
    connection.row_factory = sqlite3.Row
    # access the database using a cursor object
    return connection

@app.route('/', methods=['GET'])
def index():
    # opens the database connection
    connection = db_connection()
    # fetches all the data from the top_books table
    data = connection.execute('''SELECT * FROM top_books''').fetchall()
    # closes database connection
    connection.close()
    # render the index.html template and pass the data from the database
    return render_template('index.html', books=data)

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit_book(id):
    # opens the database connection
    connection = db_connection()
    if request.method == 'POST':
        # form data from the user
        title = request.form['title']
        price = request.form['price']
        availability = request.form['availability']
        # edits the data from the top_books table with the specified ID
        data = connection.execute('''UPDATE top_books SET title = ?, price = ?, availability = ?  WHERE id= ?''', (title, price, availability, id))
        # saves the changes
        connection.commit()
        # closes database connection
        connection.close()
        # redirects to the index.html page
        redirect(url_for('index'))
    else:
        book = connection.execute('''SELECT * FROM top_books WHERE id = ?''', (id,)).fetchone()
        connection.close()
        return render_template('edit.html', book=book)
    
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_book(id):
    # opens the database connection
    connection = db_connection()
    # deletes the data from the top_books table with the specified ID
    book = connection.execute('''DELETE FROM top_books WHERE id = ?''', (id,))
    # saves the changes
    connection.commit()
    # closes database connection
    connection.close()
    # renders delete.html page
    return render_template('delete.html', book=book)

@app.route('/add', methods=['GET','POST'])
def add_book():
    if request.method == 'POST':
        # opens the database connection
        connection = db_connection()
        # form data from the user
        title = request.form['title']
        price = request.form['price']
        availability = request.form['availability']
        # adds the data to the top_books 
        connection.execute('''INSERT INTO top_books (title, price, availability) VALUES (?, ?, ?)''', (title, price, availability))
        # saves the changes
        connection.commit()
        # closes database connection
        connection.close()
        # redirects to the index.html page
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)