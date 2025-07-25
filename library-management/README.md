# Library Management System

This project is a Library Management System that allows for the management of books and users. It provides functionalities to add, remove, and retrieve books and users, as well as manage the issuance of books.

## Project Structure

```
library-management
├── src
│   ├── models
│   │   ├── __init__.py
│   │   └── db.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── book_service.py
│   │   └── user_service.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── db_utils.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_book_service.py
│   └── test_user_service.py
├── requirements.txt
└── README.md
```

## Features

- **Database Management**: Setup and manage a SQLite database for storing book and user information.
- **Book Management**: Add, remove, and retrieve books from the library.
- **User Management**: Add, remove, and retrieve users of the library.
- **Issuance Management**: Track which users have issued which books.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd library-management
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.