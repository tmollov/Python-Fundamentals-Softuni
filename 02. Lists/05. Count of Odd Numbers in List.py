arr = input().split(" ")
oddCount = 0
for i in range(len(arr)):
    if int(arr[i]) % 2 == 1:
        oddCount += 1

print(oddCount)