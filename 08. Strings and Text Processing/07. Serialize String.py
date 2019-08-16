word = input()

dic = dict()

for i in range(len(word)):
    ch = word[i]
    if dic.__contains__(ch):
        dic[ch].append(i)
    else:
        dic.__setitem__(ch,[i])
        
for key in dic:
    indexes = '/'.join(map(str,dic[key]))
    print(f"{key}:{indexes}")