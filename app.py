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

# create new route rendering a template called details.html
@app.route('/details')
def details():
    conn = get_db_connection()
    # execute a query
    books = conn.execute('SELECT * FROM books').fetchall()
    # close the connection
    conn.close()
    return render_template('details.html', books=books)

if __name__ == '__main__': 
    app.run(debug=True) 