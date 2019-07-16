import math

class ClosePoints:
    def __init__(self, first, second, diff):
        self.First = first
        self.Second = second
        self.diff = diff

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def CalcDistance(self,secondPoint):
        a = int(math.fabs(self.x - secondPoint.x))
        b = int(math.fabs(self.y - secondPoint.y))
        result = math.sqrt((a*a)+(b*b))
        return result

count = int(input())
points = list()
closestPoints = list()

for i in range(count):
    In = input().split(" ")
    points.append(Point(int(In[0]),int(In[1])))

closest = 2147483647
closePoints = None

for p in range(len(points)):
    for i in range(len(points)):
        if p == i:
            continue
        distance = points[p].CalcDistance(points[i])
        if distance < closest :
            closest = distance
            closePoints = ClosePoints(points[p],points[i],distance)
    

print(f"{closePoints.diff:.3f}")
print(f"({closePoints.First.x}, {closePoints.First.y})")
print(f"({closePoints.Second.x}, {closePoints.Second.y})")