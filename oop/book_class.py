class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # The __str__ method should return a readable string for the user
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    
    # The __repr_
