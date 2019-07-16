import math as m

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def CalcDistance(firstPoint,secondPoint):
    a = int(m.fabs(firstPoint.x - secondPoint.x))
    b = int(m.fabs(firstPoint.y - secondPoint.y))
    result = m.sqrt((a*a)+(b*b))
    return result

fIn = input().split(" ")
sIn = input().split(" ")
point1 = Point(int(fIn[0]),int(fIn[1]))
point2 = Point(int(sIn[0]),int(sIn[1]))
result = CalcDistance(point1,point2)
print(f"{result:.3f}")