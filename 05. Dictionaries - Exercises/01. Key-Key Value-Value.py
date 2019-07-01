def Match(key,value,values):
    for val in values:
                    if val.__contains__(value):
                        dic[key].append(val)

targetKey = input()
targetValue = input()
count = int(input())

dic = dict()
for i in range(count):
    parts = input().split(" => ")
    key = parts[0]
    values = parts[1].split(";")
    
    if key.__contains__(targetKey):
        if dic.__contains__(key):
            Match(key,targetValue,values)
        else:
            dic.__setitem__(key,[]) 
            Match(key,targetValue,values)

for key in dic:
    print(f"{key}:")
    for item in dic[key]:
        print(f"-{item}")