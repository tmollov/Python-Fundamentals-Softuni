def printList(targetList):
    for i in range(len(targetList)):
        print(f"{targetList[i]}", end=" ")

def getFilteredArray(targetArray):
    resultArr = []  
    for i in range(len(targetArray)):
        a = targetArray[i].split(" ")
        resultArr.append([x for x in a if x])
    return resultArr

arr = input().split("|")
filteredArr = getFilteredArray(arr)  

for i in range(len(filteredArr),0,-1):
    printList(filteredArr[i-1])