from interface import LibraryInterface
from models.db import get_connection

class Library(LibraryInterface):
    def add_book(self, book):
        book.save_to_db()

    def add_user(self, user):
        user.save_to_db()

    def issue_book(self, book_title, user_id):
        conn = get_connection()
        cursor = conn.cursor()

        # Find available book
        cursor.execute("SELECT id FROM books WHERE title = ? AND is_issued = 0", (book_title,))
        book = cursor.fetchone()
        if book:
            book_id = book[0]
            cursor.execute("UPDATE books SET is_issued = 1 WHERE id = ?", (book_id,))
            cursor.execute("INSERT INTO issued_books (user_id, book_id) VALUES (?, ?)", (user_id, book_id))
            print(f"Issued book '{book_title}' to user {user_id}.")
        else:
            print("Book not available or already issued.")
        conn.commit()
        conn.close()

    def return_book(self, book_title, user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.id FROM books b
            JOIN issued_books i ON b.id = i.book_id
            WHERE b.title = ? AND i.user_id = ?
        """, (book_title, user_id))
        result = cursor.fetchone()
        if result:
            book_id = result[0]
            cursor.execute("DELETE FROM issued_books WHERE book_id = ? AND user_id = ?", (book_id, user_id))
            cursor.execute("UPDATE books SET is_issued = 0 WHERE id = ?", (book_id,))
            print(f"Returned book '{book_title}' from user {user_id}.")
        else:
            print("No such issued book found.")
        conn.commit()
        conn.close()
