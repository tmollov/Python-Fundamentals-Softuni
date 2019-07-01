arr = sorted(list(map(int,input().split(" "))))
target = int(input())

unner = min(target,len(arr))
lenOfArr = len(arr)-1
for i in range(lenOfArr,lenOfArr - unner,-1):
    print(arr[i],end = " ")