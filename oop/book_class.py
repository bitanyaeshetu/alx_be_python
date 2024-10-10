class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # Human-readable representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Unambiguous representation for debugging
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Called when the object is deleted
        print(f"Deleting {self.title}")

