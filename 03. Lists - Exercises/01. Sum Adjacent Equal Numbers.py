arr = list(map(float, input().split(" ")))

index = 0
while True:
    if index < len(arr) - 1:
        if arr[index] == arr[index+1]:
            arr[index] = arr[index]+arr[index+1]
            arr.remove(arr[index+1])
            index = 0
        else:
            index += 1
    else :
        break
print(" ".join([str(item) for item in arr]))