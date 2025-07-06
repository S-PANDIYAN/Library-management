from library import Library
from user import Student, Staff
from book import Book
from db import setup_database

def main():
    setup_database()
    lib = Library()

    # Sample users
    lib.add_user(Student(1, "Alice"))
    lib.add_user(Staff(2, "Dr. Bob"))

    while True:
        print("\n--- College Library Menu ---")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            lib.add_book(Book(title, author))
            print("Book added.")
        elif choice == '2':
            books = Book.get_available_books()
            if books:
                print("Available Books:")
                for b in books:
                    print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}")
            else:
                print("No books available.")
        elif choice == '3':
            title = input("Book to issue: ")
            user_id = int(input("User ID: "))
            lib.issue_book(title, user_id)
        elif choice == '4':
            title = input("Book to return: ")
            user_id = int(input("User ID: "))
            lib.return_book(title, user_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
