target = list(input())

def Left(count):
    for i in range(count):
        last = target.pop(0)
        target.append(last)
        
def Right(count):
    for i in range(count):
        last = target.pop()
        target.insert(0,last)
        
def Insert(index,string):
    for ch in string[::-1]:
        target.insert(index,ch)
        
def Delete(start,end):
   del target[start:end+1]

while True:
    command = input().split(" ")
    if command[0] == "end":
        break

    if command[0] == "Left":
        Left(int(command[1]))
    elif command[0] == "Right":
        Right(int(command[1]))
    elif command[0] == "Delete":
        Delete(int(command[1]),int(command[2]))
    elif command[0] == "Insert":
        Insert(int(command[1]),command[2])
print("".join(target))