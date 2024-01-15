# library.py
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author.name}, Year: {book.year}")

    # Other library management methods
    # ...
