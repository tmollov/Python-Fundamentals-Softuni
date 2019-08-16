arr = list(map(int,input().split(" ")))

def Excange(count):
    global arr
    if count > len(arr) or count <= 0:
        print("Invalid index")
        return
    count+=1
    l1 = arr[:count]
    l2 = arr[count:]
    arr = l2 + l1
        
def Max(maxT):
    maxN = -1
    index = -1
    if maxT == "odd":
        for i in range(len(arr)):
            if arr[i] % 2 == 1 and arr[i] >= maxN:
                maxN = arr[i]
                index = i
    elif maxT == "even":
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= maxN:
                maxN = arr[i]
                index = i
    if index == -1:
        print("No matches")
        return
    print(index)

def Min(maxT):
    minN = 51
    index = -1
    if maxT == "odd":
        for i in range(len(arr)):
            if arr[i] % 2 == 1 and arr[i] <= minN:
                minN = arr[i]
                index = i
    elif maxT == "even":
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] <= minN:
                minN = arr[i]
                index = i
    if index == -1:
        print("No matches")
        return
    print(index)

def First(count,numT):
    if count > len(arr):
        print("Invalid count")
        return
    
    nums = []
    if numT == "odd":
        nums = list(filter(lambda x: x % 2 == 1,arr))[:count]
    elif numT == "even":
        nums = list(filter(lambda x: x % 2 == 0,arr))[:count]
    print(nums)

def Last(count,numT):
    if count > len(arr):
        print("Invalid count")
        return
    
    nums = []
    if numT == "odd":
        nums = list(filter(lambda x: x % 2 == 1,arr))[-count:]
    elif numT == "even":
        nums = list(filter(lambda x: x % 2 == 0,arr))[-count:]
    print(nums)

while True:
    command = input().split(" ")
    if command[0] == "end":
        break

    if command[0] == 'exchange':
        Excange(int(command[1]))
    elif command[0] == 'max':
        Max(command[1])
    elif command[0] == 'min':
        Min(command[1])
    elif command[0] == 'first':
        First(int(command[1]),command[2])
    elif command[0] == 'last':
        Last(int(command[1]),command[2])
    
print(arr)