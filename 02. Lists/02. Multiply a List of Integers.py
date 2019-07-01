arr = input().split(" ")
multiplier = int(input())
for i in range(len(arr)):
    arr[i] = int(arr[i]) * multiplier

print(" ".join(str(x) for x in arr))