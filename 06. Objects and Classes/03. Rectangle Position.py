class Rectangle:
    def __init__(self, left, right, width, height):
        self.left = left
        self.right = right
        self.bottom = right + height
        self.top = left + width

    def IsInsideOf(self, rectangle):
        if self.left >= rectangle.left and \
           self.right <= rectangle.right and \
           self.top <= rectangle.top and \
           self.bottom <= rectangle.bottom:
            return True
        return False
    

fRect = list(map(int,input().split(" ")))
sRect = list(map(int,input().split(" ")))

firstRectangle = Rectangle(fRect[0],fRect[1],fRect[2],fRect[3])
secondRectangle = Rectangle(sRect[0],sRect[1],sRect[2],sRect[3])
if firstRectangle.IsInsideOf(secondRectangle):
    print("Inside")
else:
    print("Not inside")