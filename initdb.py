import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",
            ('Frankenstein', 'Mary Shelley', 'science fiction')
            )
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",
            ('Women in Love', 'D.H. Lawrence', 'modernist')
            )
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",
            ('Wuthering Heights', 'Emily Bronte', 'gothic')
            )

connection.commit()
connection.close()