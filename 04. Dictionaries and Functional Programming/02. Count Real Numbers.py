sequence = sorted([float(item) for item in input().lower().split(" ")])

dic = dict()

for el in sequence:
        if not dic.__contains__(el):
                dic.__setitem__(el,1)
        else:
                dic[el] += 1
for el in dic:
        print(f"{el} -> {dic[el]} times")