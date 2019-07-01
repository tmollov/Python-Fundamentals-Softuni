arr = input().split(" ")
pozitiveArr = []
for i in range(len(arr)):
    currNum = int(arr[i]) 
    if currNum > 0:
        pozitiveArr.append(currNum)

if len(pozitiveArr) < 1:
    print("empty")
    exit()
print(" ".join(str(x) for x in reversed(pozitiveArr)))