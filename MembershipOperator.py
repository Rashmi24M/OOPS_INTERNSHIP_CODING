class Library:
    def __init__(self):
        self.books = []
    def __contains__(self,books):
        return books in self.books # it return true
library = Library()
library.books.append("Python")
library.books.append("Java")
library.books.append("C++")

print("Python" in library) 