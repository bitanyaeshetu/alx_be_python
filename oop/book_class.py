class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Update __str__ to match expected format without quotes around the title
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    # Keep __repr__ as it is since it matches the expected format
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    # Optionally, include a __del__ method if you want to print a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

# Example usage
book = Book("1984", "George Orwell", 1949)

print(book)        # Calls __str__, output: 1984 by George Orwell, published in 1949
print(repr(book))  # Calls __repr__, output: Book('1984', 'George Orwell', 1949)

# When the object is deleted, __del__ method will print: Deleting 1984
