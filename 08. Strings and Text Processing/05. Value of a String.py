word = input()
target = input().lower()

upper = [65,90]
lower = [97,122]

result = list(map(lambda x: ord(x), word))
if target == "uppercase":
    result = sum(list(filter(lambda x: x >= upper[0] and x <= upper[1],result)))
else:
    result = sum(list(filter(lambda x: x >= lower[0] and x <= lower[1],result)))
print(f'The total sum is: {result}')