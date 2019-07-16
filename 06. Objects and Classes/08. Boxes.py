import math as m

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def CalcDistance(self,secondPoint):
        a = int(m.fabs(self.x - secondPoint.x))
        b = int(m.fabs(self.y - secondPoint.y))
        result = m.sqrt((a*a)+(b*b))
        return result

class Box:
    def __init__(self,upperLeft,upperRight,bottomLeft,bottomRight):
        self.upperLeft = upperLeft
        self.upperRight = upperRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        self.width = self.upperLeft.CalcDistance(self.upperRight) 
        self.height = self.upperLeft.CalcDistance(self.bottomLeft)

    def CalculatePerimeter(self):
        return int((2*self.width) + (2*self.height))
    
    def CalculateArea(self):
        return int(self.width * self.height)
    
    def Print(self):
        print(f"Box: {self.width:.0f}, {self.height:.0f}")
        print(f"Perimeter: {self.CalculatePerimeter()}")
        print(f"Area: {self.CalculateArea()}")

while True:
    info = input().split(" | ")
    if len(info) == 1:
        break
    p = []
    for el in info:
        coor = list(map(int,el.split(":")))
        p.append(Point(coor[0],coor[1]))

    box = Box(p[0],p[1],p[2],p[3])
    box.Print()