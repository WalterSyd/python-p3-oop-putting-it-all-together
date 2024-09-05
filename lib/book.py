#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        #has the title and page_count passed into __init__, and values can be set to new instance.
        self.title = title
        self.page_count = None
        self.page_count = page_count


    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
             print("page_count must be an integer\n", end="")
        else:
            self._page_count = value


    def turn_page(self):
       # outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
       print("Flipping the page...wow, you read fast!")

# book1 = Book("And Then There Were None", 272)
# book1.page_count = "not an integer"
     

# print(book1.title)
# print(book1.page_count)