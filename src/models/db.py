import sqlite3

def get_connection():
    return sqlite3.connect("data/library.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        is_issued INTEGER DEFAULT 0
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issued_books (
        user_id INTEGER,
        book_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(book_id) REFERENCES books(id)
    )
    ''')

    conn.commit()
    conn.close()
