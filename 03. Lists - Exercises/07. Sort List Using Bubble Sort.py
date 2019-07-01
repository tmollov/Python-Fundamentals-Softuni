def bubbleSort(alist):
    for num in range(len(alist)-1,0,-1):
        for i in range(num):
            if alist[i]>alist[i+1]:
                swap = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = swap

arr = list(map(int,input().split(" ")))
bubbleSort(arr)
print(" ".join([str(item) for item in arr]))