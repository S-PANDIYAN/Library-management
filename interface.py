from abc import ABC, abstractmethod

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def issue_book(self, book_title, user_id):
        pass

    @abstractmethod
    def return_book(self, book_title, user_id):
        pass
