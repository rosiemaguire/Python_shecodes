class Book:
    
    def __init__(self,title,author,pages,current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def bookmark_page(self):
        self.bookmark = self.current_page

    def turn_page(self):
        self.current_page += 1
    
my_book = Book("A great book","me")
print(my_book)