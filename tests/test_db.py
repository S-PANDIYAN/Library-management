"""Test suite for database operations"""
import pytest
import os
from pathlib import Path
import sqlite3
from src.models.db import setup_database, get_connection
from src.models.book import Book
from src.models.user import User

@pytest.fixture(scope="function")
def test_db():
    """Fixture to create a test database in memory"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create tables using model classes
    Book.create_table(cursor)
    User.create_table(cursor)
    
    # Create issued_books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issued_books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        return_date TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(book_id) REFERENCES books(id)
    )
    ''')
    
    conn.commit()
    yield conn
    conn.close()

def test_database_creation(tmp_path):
    """Test database creation and table setup"""
    # Setup a temporary data directory
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    
    # Run the database setup
    setup_database()
    
    # Connect to the database and check tables
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {table[0] for table in cursor.fetchall()}
    
    # Verify all required tables exist
    assert 'books' in tables
    assert 'users' in tables
    assert 'issued_books' in tables
    
    conn.close()

def test_book_operations(test_db):
    """Test book table operations"""
    cursor = test_db.cursor()
    
    # Insert a test book
    cursor.execute(
        "INSERT INTO books (title, author, is_issued) VALUES (?, ?, ?)",
        ("Test Book", "Test Author", 0)
    )
    test_db.commit()
    
    # Verify the book was inserted
    cursor.execute("SELECT title, author, is_issued FROM books WHERE id = 1")
    book = cursor.fetchone()
    assert book == ("Test Book", "Test Author", 0)

def test_user_operations(test_db):
    """Test user table operations"""
    cursor = test_db.cursor()
    
    # Insert a test user
    cursor.execute(
        "INSERT INTO users (name, type) VALUES (?, ?)",
        ("Test User", "student")
    )
    test_db.commit()
    
    # Verify the user was inserted
    cursor.execute("SELECT name, type FROM users WHERE id = 1")
    user = cursor.fetchone()
    assert user == ("Test User", "student")
