age = dict()
salary = dict()
position = dict()

filterType = ""
while True:
    string = input()
    if string == "filter base":
        filterType = input()
        break
    
    parts = string.split(" -> ")
    key = parts[0]
    value = parts[1]

    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
            if int(value) == float(value):
                value = int(value)
        except ValueError:
            value
               
    if type(value) == int:
        age.__setitem__(key,value)
    elif type(value) == float:
        salary.__setitem__(key,value)
    else :
        position.__setitem__(key,value)

result = None
if filterType == "Position":
    result = position
elif filterType == "Age" :
    result = age
else :
    result = salary

for key in result:
    print(f"Name: {key}")
    print(f"{filterType}: {result[key]}")
    print(20*"=")