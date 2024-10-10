class Book:
  """
  A class representing a book with title, author, and year attributes.
  """
  def __init__(self, title, author, year):
    """
    Initializes a Book instance with title, author, and year.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.
    """
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    """
    Returns a string in the format 'title by author, published in year'."""
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string that would recreate the Book instance."""
    return f"Book('{self.title}', '{self.author}', {self.year})"

  def __del__(self):
    """
    Prints 'Deleting (title of the book)' upon object deletion."""
    print(f"Deleting {self.title}")

# Create a book instance
book = Book("1984", "George Orwell", 1949)

# Print book details using __str__ and __repr__
print(book)  # Expected: 1984 by George Orwell, published in 1949
print(repr(book))  # Expected: Book('1984', 'George Orwell', 1949)

# Delete the book instance
del book  # Expected: Deleting 1984