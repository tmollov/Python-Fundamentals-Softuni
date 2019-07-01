import re 

regex = r"\W+ = [0-9]+|\w+ = [0-9]+"
dic = dict()
while True:
    string = input()
    if string == "end":
        break
    info = string.split(" = ")
    key = info[0]
    value = info[1]

    if re.findall(regex,string):
        dic.__setitem__(key,int(value))
    else:
        if dic.__contains__(value):
            dic[key] = dic[value]
            
for key in dic:
    print(f"{key} === {dic[key]}")