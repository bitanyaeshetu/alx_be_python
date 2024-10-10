# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str
