"""User model for the library management system"""

class User:
    def __init__(self, id=None, name=None, type=None):
        self.id = id
        self.name = name
        self.type = type

    @staticmethod
    def create_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL
        )
        ''')
