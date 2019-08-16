data = dict()

for i in range(int(input())):
    for i in list(input()):
        if data.__contains__(i):
            data[i] += 1
        else:
            data.__setitem__(i,1) 

maxed = []

for key in data:
    if len(maxed) == 0:
        maxed.append(key)
        maxed.append(data[key])
    elif maxed[1] < data[key]:
        maxed[0] = key
        maxed[1] = data[key]
    
if data.__len__() == 1:
    maxed[1] = maxed[1] / 2

count = 1
out = 0 + count
while True:
    if maxed[1] < out:
        break
    print(maxed[0]*count)
    count += 2
    out += count