import re 

regex = r"^[0-9]+"
dic = dict()
while True:
    string = input()
    if string == "Over":
        break
    info = string.split(" : ")
    key = info[0]
    value = info[1]

    if re.findall(regex,key):
        dic.__setitem__(value,key)
    else:
        dic.__setitem__(key,value)

names = sorted(dic.keys())
for key in names:
    print(f"{key} -> {dic[key]}")