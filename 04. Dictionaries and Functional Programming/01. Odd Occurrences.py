sequence = input().lower().split(" ")

dic = dict()

for el in sequence:
        if not dic.__contains__(el):
                dic.__setitem__(el,1)
        else:
                dic[el] += 1
resultArr = []
for el in dic:
        if dic[el] % 2 == 1:
                resultArr.append(el)

print(", ".join(resultArr))