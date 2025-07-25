"""Book model for the library management system"""


class Book:
    def __init__(self, id=None, title=None, author=None, is_issued=0):
        self.id = id
        self.title = title
        self.author = author
        self.is_issued = is_issued

    @staticmethod
    def create_table(cursor):
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            is_issued INTEGER DEFAULT 0
        )
        """
        )
