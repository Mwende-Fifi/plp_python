# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        return f"Reading '{self.title}' by {self.author}."


# Child class (inherits from Book)
class ComicBook(Book):
    def __init__(self, title, author, illustrator):
        super().__init__(title, author)  # use parent constructor
        self.illustrator = illustrator

    # new method just for ComicBook
    def show_illustrations(self):
        return f"Enjoying illustrations by {self.illustrator} in '{self.title}'."


# Example usage
book1 = Book("1984", "George Orwell")
comic1 = ComicBook("Spider-Man", "Stan Lee", "Steve Ditko")

print(book1.read())
print(comic1.read())
print(comic1.show_illustrations())
