import sys, os
from flask import Flask, render_template, request, render_template_string
import sqlite3
from flask_flatpages import FlatPages
import functions

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(__name__)
app.config['FLATPAGES_HTML_RENDERER'] = functions.my_renderer
pages = FlatPages(app)

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

# URL Routing - Flat Pages
# Retrieves the page path and
@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

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

def get_tag_list(genre):
    conn = get_db_connection()
    # execute a query
    books = conn.execute('SELECT * FROM books WHERE genre = ?', (genre,)).fetchall()
    conn.close()
    if books is None:
        abort(404)
    return books

@app.route('/tag/<genre>')
def tag_list(genre):
    books = get_tag_list(genre)
    return render_template('tag.html', books=books)


if __name__ == '__main__': 
    app.run(debug=True) 