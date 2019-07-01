arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()

print(' <= '.join(str(x) for x in arr))