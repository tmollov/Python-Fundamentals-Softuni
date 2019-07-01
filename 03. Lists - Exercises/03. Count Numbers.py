arr = sorted(list(map(int, input().split(" "))))
dic = dict()

for num in arr:
    if dic.__contains__(num):
        dic[num]+=1
    else:
        dic.__setitem__(num,1)

for key in dic:
    print(f"{key} -> {dic[key]}")