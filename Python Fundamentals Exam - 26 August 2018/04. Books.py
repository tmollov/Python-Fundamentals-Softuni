import re
from functools import reduce

personCheck = r"^(\w+)\s(\w+)\s(\w+.*\w*)$"
chapterCheck = r"\b(\w+),*\s*\b"
class Book():
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price
        self.chapters = []
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value <= 0:
            raise Exception("Negative Price!")
        self._price = value
        
    def AddChapters(self,arr):
        self.chapters += arr

db = dict()

while True:
    line = input()
    if line == "on work":
        break
    
    parts = list(map(lambda x:x.strip(), line.split(" -> ")))
    personInfo = list(filter(lambda x: x != "", parts[0].split(" ")))
    chapters = parts[1].split(", ")
    if not re.findall(personCheck,parts[0]) and \
        not len(re.findall(chapterCheck,parts[1])) == len(chapters):
        continue
    
    try:   
        p = Book(personInfo[0],personInfo[1],float(personInfo[2]))
        p.AddChapters(chapters)
        if db.__contains__(p.name):
            db[p.name] = p
        else:
            db.__setitem__(p.name,p)
    except Exception as e:
        continue

sold = []
notFoundedBooks = 0
while True:
    bookName = input()
    
    if bookName == "end work":
        break
    
    if db.__contains__(bookName) :
        sold.append(db[bookName])
    else:
        notFoundedBooks += 1
        
print("No such book here\n" * notFoundedBooks, end="")

if sold:
    for book in sold:
        print(f"SOLD: {book.name} with author {book.author}. Chapters in the book {len(book.chapters)}")
    money = sum(map(lambda x:x.price,sold))
    print(f"Money: {money:.2f}")
else:
    print("Bad day :(")