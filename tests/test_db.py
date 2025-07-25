import pytest
import os
import sqlite3
from src.models.db import setup_database, get_connection

@pytest.fixture
def test_db():
    # Use an in-memory database for testing
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create test tables
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
    return conn

def test_database_creation():
    # Remove test database if it exists
    if os.path.exists("data/library.db"):
        os.remove("data/library.db")
    
    # Run the database setup
    setup_database()
    
    # Check if database file was created
    assert os.path.exists("data/library.db")
    
    # Check if tables were created
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    
    assert 'books' in table_names
    assert 'users' in table_names
    assert 'issued_books' in table_names
    
    conn.close()

def test_database_connection(test_db):
    # Test if we can insert and retrieve data
    cursor = test_db.cursor()
    
    # Insert test data
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", 
                  ("Test Book", "Test Author"))
    test_db.commit()
    
    # Retrieve test data
    cursor.execute("SELECT title, author FROM books WHERE id = 1")
    book = cursor.fetchone()
    
    assert book[0] == "Test Book"
    assert book[1] == "Test Author"
