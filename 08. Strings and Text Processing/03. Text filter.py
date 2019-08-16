targets = input().split(" ")
text = input()

for target in targets:
    newOne = "*" * len(target)
    text = text.replace(target,newOne)
    
print(text)