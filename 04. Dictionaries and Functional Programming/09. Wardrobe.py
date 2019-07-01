count = int(input())

colorDic = dict()

for i in range(count):
    parts = input().split(" -> ")
    color = parts[0]
    items = parts[1].split(",")

    if colorDic.__contains__(color):
        for item in items:
            if item == "":
                continue
            if colorDic[color].__contains__(item):
                colorDic[color][item] += 1
            else :
                colorDic[color].__setitem__(item,1)
    else:
        colorDic.__setitem__(color,dict())
        for item in items:
            if colorDic[color].__contains__(item):
                colorDic[color][item] += 1
            else :
                colorDic[color].__setitem__(item,1)
targets = input().split(" ")

for color in colorDic:
    print(f"{color} clothes:")
    for item in colorDic[color]:
        if color == targets[0] and item == targets[1]:
            print(f"* {item} - {colorDic[color][item]} (found!)")
        else:
            print(f"* {item} - {colorDic[color][item]}")