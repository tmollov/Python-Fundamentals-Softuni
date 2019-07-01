def compare(left,right):
    if left > right:
        return left
    else:
        return right

varType = input()
left = None
right = None

if varType == "int":
    left = int(input())
    right = int(input())
elif varType == "float" :
    left = float(input())
    right = float(input())
else :
    left = input()
    right = input()

result = compare(left,right)
print(result)