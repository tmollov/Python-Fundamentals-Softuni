import re

def IsLowerCase(word):
    if re.findall(r"^[a-z]+$",word):
        return True
    return False

def IsUpperCase(word):
    if re.findall(r"^[A-Z]+$",word):
        return True
    return False

sentence = input()
regex = r"[^[,;:.!()\"\'\\\/[\] ]+"
matches = re.findall(regex, sentence)

lowerCaseArr = []
mixedCaseArr = []
upperCaseArr = []

for word in matches:
    if IsLowerCase(word):
        lowerCaseArr.append(word)
    elif IsUpperCase(word):
        upperCaseArr.append(word)
    else :
        mixedCaseArr.append(word)

seperator = ", "
print(f"Lower-case: {seperator.join(lowerCaseArr)}")
print(f"Mixed-case: {seperator.join(mixedCaseArr)}")
print(f"Upper-case: {seperator.join(upperCaseArr)}")