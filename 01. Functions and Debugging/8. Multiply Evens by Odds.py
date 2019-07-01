def findEvenSum(stringOfNumber):
    sum = 0
    num = 0
    for i in stringOfNumber:
        num = int(i)
        if int(i) % 2 == 0:
            sum += num
    return sum

def findOddSum(stringOfNumber):
    sum = 0
    num = 0
    for i in stringOfNumber:
        num = int(i)
        if int(i) % 2 == 1:
            sum += num
    return sum

number = input().replace("-","")
evenSum = findEvenSum(number)
oddSum = findOddSum(number)
print(evenSum*oddSum)