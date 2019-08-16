data = dict()

while True:
    dat = input().split(":")
    if dat[0] == "end":
        break

    ch = dat[0]
    indexes = list(map(int,dat[1].split("/")))
    for i in indexes:
        data.__setitem__(i,ch)
    
for key in sorted(data.keys(), key=lambda x: x, ):
    print(data[key], end="")