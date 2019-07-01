shop = dict()

while True:
    string = input()
    if string == "shopping time":
        break
    
    info = string.split(" ")
    key = info[1]
    value = int(info[2])
    if shop.__contains__(key):
        shop[key] += value
    else :
        shop.__setitem__(key,value)

while True:
    string = input()
    if string == "exam time":
        break
    
    info = string.split(" ")
    targetKey = info[1]
    targetValue = int(info[2])
    if shop.__contains__(targetKey):
        if shop[targetKey] == 0:
            print(f"{targetKey} out of stock")
        elif shop[targetKey] < targetValue:
            shop[targetKey] = 0
        else:
            shop[targetKey] -= targetValue
    else :
        print(f"{targetKey} doesn't exist")

for product in shop:
    if shop[product] <= 0:
        continue
    else:
        print(f"{product} -> {shop[product]}")