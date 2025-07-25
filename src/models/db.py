"""Database configuration and setup for the library management system"""
import sqlite3
import os
from pathlib import Path
from .book import Book
from .user import User

def get_connection():
    """Get a connection to the SQLite database"""
    # Get the absolute path to the data directory
    base_dir = Path(__file__).resolve().parent.parent.parent
    data_dir = base_dir / "data"
    # Ensure data directory exists
    data_dir.mkdir(exist_ok=True)
    # Connect to database
    return sqlite3.connect(str(data_dir / "library.db"))

def setup_database():
    """Initialize the database with required tables"""
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables using model classes
    Book.create_table(cursor)
    User.create_table(cursor)

    # Create issued books table
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
    conn.close()
