class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("Title:",self.title,"Author:",self.author)
class IssuedBook(Book):
    def __init__(self,issued_to,issued_date,title,author):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_issued_book_details(self):
        self.display_book_details() #No need  of super here  because we already iherited by book class and also initialise values to that parent class varibales in child class only then we can directly access using how we access its own class attrbute using self like issued date and issued to info
        print("Issued To  :", self.issued_to)
        print("Issued Date:", self.issued_date)

        
        
    
issued_book = IssuedBook(
    "Python Programming",
    "Robert C. Martin",
    "Rashmi",
    "04-02-2026"
)
issued_book.display_issued_book_details()