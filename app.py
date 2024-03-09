from flask import Flask, render_template, request 
import sqlite3

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def get_db_connection():
    # connect to the database
    conn = sqlite3.connect('database.db')
    # sets the row_factory attribute to sqlite3.Row so you can have name-based access to columns
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # execute a query
    books = conn.execute('SELECT * FROM books').fetchall()
    # close the connection
    conn.close()
    return render_template('index.html', books=books)

def get_details(book_id):
    conn = get_db_connection()
    # execute a query
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    if book is None:
        abort(404)
    return book

@app.route('/<int:book_id>')
def details(book_id):
    book = get_details(book_id)
    return render_template('details.html', book=book)

if __name__ == '__main__': 
    app.run(debug=True) 