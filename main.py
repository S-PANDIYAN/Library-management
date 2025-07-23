from controllers.library import Library
from models.user import Student, Staff
from models.book import Book
from models.db import setup_database
from views import cli_view

def main():
    setup_database()
    lib = Library()

    # Sample users
    lib.add_user(Student(1, "Alice"))
    lib.add_user(Staff(2, "Dr. Bob"))

    while True:
        cli_view.show_menu()
        choice = cli_view.get_menu_choice()

        if choice == '1':
            title, author = cli_view.get_book_details()
            lib.add_book(Book(title, author))
            cli_view.show_message("Book added.")
        elif choice == '2':
            books = Book.get_available_books()
            cli_view.show_available_books(books)
        elif choice == '3':
            title = cli_view.get_book_title()
            user_id = cli_view.get_user_id()
            lib.issue_book(title, user_id)
        elif choice == '4':
            title = cli_view.get_book_title()
            user_id = cli_view.get_user_id()
            lib.return_book(title, user_id)
        elif choice == '5':
            cli_view.show_message("Exiting...")
            break
        else:
            cli_view.show_message("Invalid choice.")

if __name__ == "__main__":
    main()
