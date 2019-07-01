def printBorder(length):
    print("-" * length * 2)

def printBody(length):
    innerStr = '\/' * (length-1)
    print(f"-{innerStr}-")

length = int(input())

printBorder(length)
for i in range(length-2):
    printBody(length)
printBorder(length)