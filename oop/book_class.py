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

    def __str__(self):
        """String representation for printing a readable description."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example of creating a book instance
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)
    print(str(book))  # Output: '1984' by George Orwell, published in 1949
    print(repr(book))  # Output: Book('1984', 'George Orwell', 1949)
