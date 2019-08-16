import re

def GetReg(times):
    res = "([a-zA-Z]{"+ str(times) + "})"
    regex = rf"^([0-9]*){res}([^a-zA-Z]*$)"
    return regex

def GetPart(key,target):
    arr = []
    for ch in key:
        if ord(ch) >= 48 and ord(ch) <= 57:
            index = int(ch)
            if index >= 0 and index < len(target):
                arr.append(target[index])
            else:
                arr.append(" ")
        else:
            arr.append(" ")
    return arr

while True:
    line = input()
    if line == "Over!":
        break
    times = int(input())
    regex = GetReg(times)
    matches = re.findall(regex,line)
    if matches:
        firstKey = matches[0][0]
        secondKey = matches[0][2]
        target = matches[0][1]
        
        decryptedLine = GetPart(firstKey,target) + GetPart(secondKey,target)
        print(f"{target} == {''.join(decryptedLine)}")