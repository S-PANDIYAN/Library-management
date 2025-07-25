import unittest
from src.services.book_service import add_book, remove_book, get_books
from src.models.db import setup_database

class TestBookService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setup_database()

    def test_add_book(self):
        result = add_book("Test Book", "Test Author")
        self.assertTrue(result)

    def test_get_books(self):
        books = get_books()
        self.assertIsInstance(books, list)

    def test_remove_book(self):
        add_book("Book to Remove", "Author")
        result = remove_book("Book to Remove")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()