from models.db import get_connection


class User:
    def __init__(self, user_id, name, user_type):
        self.user_id = user_id
        self.name = name
        self.user_type = user_type

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (id, name, type) VALUES (?, ?, ?)",
                       (self.user_id, self.name, self.user_type))
        conn.commit()
        conn.close()

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "Student")

class Staff(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "Staff")
