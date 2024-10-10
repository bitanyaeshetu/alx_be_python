class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Human-readable representation
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        # Unambiguous, often useful for debugging
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __del__(self):
        # Called when the object is deleted
        print(f"Book '{self.title}' is being deleted.")
