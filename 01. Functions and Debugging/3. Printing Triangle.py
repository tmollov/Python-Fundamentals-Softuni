def printLine(start,end):
    for i in range(start, end + 1):
        print(i, end=' ')
    print()

def printTriangle(size):
    for i in range(1, size):
        printLine(1,i)
    for i in range(size,0,-1):
        printLine(1,i)

size = int(input())

printTriangle(size)