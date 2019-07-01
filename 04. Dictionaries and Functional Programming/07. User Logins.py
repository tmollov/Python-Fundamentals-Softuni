hosting = dict()

while True:
    string = input()
    if string == "login":
        break
    
    info = string.split(" -> ")
    key = info[0]
    value = info[1]
    if hosting.__contains__(key):
        hosting[key] = value
    else :
        hosting.__setitem__(key,value)

unsuccesfulLogins = 0
while True:
    string = input()
    if string == "end":
        break
    
    info = string.split(" -> ")
    targetKey = info[0]
    targetValue = info[1]
    if hosting.__contains__(targetKey):
        if hosting[targetKey] == targetValue:
            print(f"{targetKey}: logged in successfully")
        else: 
            print(f"{targetKey}: login failed")
            unsuccesfulLogins += 1
    else:
        print(f"{targetKey}: login failed")
        unsuccesfulLogins += 1
print(f"unsuccessful login attempts: {unsuccesfulLogins}")