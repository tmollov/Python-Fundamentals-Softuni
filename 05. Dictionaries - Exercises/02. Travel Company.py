seats = dict()

def GetQuantity(dictionary):
    qty = 0
    for key in dictionary:
        qty += dictionary[key]
    return qty

while True:
    parts = input().split(":")
    if len(parts) == 1:
        break
    city = parts[0]
    transportations = parts[1].split(",")

    if seats.__contains__(city):
        for item in transportations:
            key = item.split("-")
            value = int(key[1])
            if seats[city].__contains__(key[0]):
                seats[city][key[0]] = value
            else:
                seats[city].__setitem__(key[0],value)
    else :
        seats.__setitem__(city,dict())
        for item in transportations:
            key = item.split("-")
            value = int(key[1])
            if seats[city].__contains__(key[0]):
                seats[city][key[0]] = value
            else:
                seats[city].__setitem__(key[0],value)

while True:
    command = input().split(" ")
    if command[0] == "travel" and command[1] == "time!":
        break
    city = command[0]
    qnty = int(command[1])
    avail = GetQuantity(seats[city])
    if avail >= qnty:
        print(f"{city} -> all {qnty} accommodated")
    else :
        print(f"{city} -> all except {qnty - avail} accommodated")