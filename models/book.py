from models.db import get_connection

class Book:
    def __init__(self, title, author, book_id=None):
        self.title = title
        self.author = author
        self.id = book_id

    def save_to_db(self):
        conn = get_connection()
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (self.title, self.author))
        conn.commit()
        conn.close()

    @staticmethod
    def get_available_books():
        conn = get_connection()
        books = conn.execute("SELECT id, title, author FROM books WHERE is_issued = 0").fetchall()
        conn.close()
        return books
