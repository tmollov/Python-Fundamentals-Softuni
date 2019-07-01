dic = dict()

while True:
    string = input()
    if string == "end":
        break
    info = string.split(" -> ")
    key = info[0]
    values = info[1]
    try:
        values = [int(num) for num in info[1].split(", ")]
    except Exception:
        if dic.__contains__(values):
                if dic.__contains__(key):
                    dic[key] = list(dic[values])
                else:
                    dic.__setitem__(key,list(dic[values]))
        continue

    if dic.__contains__(key):
        dic[key] += values
    else:
        dic.__setitem__(key,[])
        dic[key] += values

seperator = ", "
for key in dic:
    print(f"{key} === {seperator.join([str(x) for x in dic[key]])}")