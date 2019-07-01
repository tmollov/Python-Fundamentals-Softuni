def getTriangleArea(a,h):
    return (a*h)/2

a = float(input())
h = float(input())
area = getTriangleArea(a,h)
print(f"{area:.12g}")