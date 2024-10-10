class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # String representation for human-readable format
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation to recreate the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    # Destructor to print a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

# Create a book instance
book = Book("1984", "George Orwell", 1949)

# Print book details using __str__ and __repr__
print(book)        # Expected: 1984 by George Orwell, published in 1949
print(repr(book))  # Expected: Book('1984', 'George Orwell', 1949)

# Delete the book instance
del book
