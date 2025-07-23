def show_menu():
    print("\n--- College Library Menu ---")
    print("1. Add Book")
    print("2. View Available Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

def get_menu_choice():
    return input("Enter choice: ")

def get_book_details():
    title = input("Book Title: ")
    author = input("Author: ")
    return title, author

def get_user_id():
    return int(input("User ID: "))

def get_book_title():
    return input("Book Title: ")

def show_available_books(books):
    if books:
        print("Available Books:")
        for b in books:
            print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}")
    else:
        print("No books available.")

def show_message(msg):
    print(msg)
