class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        newLine = "\n"
        tip = f"Type: {self.name()}{newLine}"   
        titl = f"Title: {self.title}{newLine}"
        auth = f"Author: {self.author}{newLine}"
        prc = f"Price: {self.price:.2f}"
        return f"{tip}{titl}{auth}{prc}"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if(len(value) < 3):
            raise Exception("Title not valid!")
        else:
            self._title = value
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,value):
        parts = value.split(" ")
        if len(parts) > 1:
            if parts[1][0] in ['1','2','3','4','5','6','7','8','9','0']:
                raise Exception("Author not valid!")
            else:
                self._author = value
        else:
            self._author = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value <= 0:
            raise Exception("Price not valid!")
        else:
            self._price = value

    def name(self):
        return type(self).__name__
    

class GoldenEditionBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author,price + (price * 0.3))

try:
    author = input()
    title = input()
    price = float(input())
    book = Book(title,author,price)
    gBook = GoldenEditionBook(title,author,price)
    print(book.__str__())
    print()
    print(gBook.__str__())
except Exception as e:
    print(str(e))