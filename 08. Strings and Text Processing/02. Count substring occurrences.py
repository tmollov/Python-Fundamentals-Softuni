text = input().lower()
target = input().lower()

occurrences = 0

for i in range(len(text)):
    endIndex = i+len(target)
    currText = text[i:endIndex]
    if currText == target:
        occurrences += 1
    
print(occurrences)