from lib.models import Book, Genre, Author

def get_all_books():
    return Book.query.get_all()