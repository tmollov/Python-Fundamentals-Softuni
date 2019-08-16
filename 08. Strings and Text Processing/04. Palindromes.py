data = input().split()

palindromes = []

for i in data:
    revers  = i[::-1]
    if i == revers and i not in palindromes:
        palindromes.append(i)

palindromes = sorted( palindromes, key=lambda x: x.lower())

print(", ".join(palindromes))