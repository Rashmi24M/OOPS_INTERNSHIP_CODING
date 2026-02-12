class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Price: ${self.price}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"
    
obj1=Book("The Great Gatsby","F. Scott Fitzgerald",10.99)
obj2=Book("To Kill a Mockingbird","Harper Lee",8.99)
print(obj1)
print(obj2)