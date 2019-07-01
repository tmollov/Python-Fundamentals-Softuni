import math as m

arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()

for num in reversed(arr):
    if num < 1:
        continue
    if m.sqrt(num) == int(m.sqrt(num)):
        print(num, end=" ") 