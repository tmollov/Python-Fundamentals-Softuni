sentence = input()
dic = dict()

for char in sentence:
    if dic.__contains__(char):
        dic[char] += 1
    else :
        dic.__setitem__(char,1)

for key in dic:
    print(f"{key} -> {dic[key]}")