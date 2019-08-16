import re

regex = r"(^[A-Z])(.+)(\.|!|\?)$"

target = input()
targetChar = target[0]
targetQty = int(target[1])

result = []

while True:
    sentence = input()
    if sentence == "end":
        break
    match = re.findall(regex,sentence)
    if match:
        wordRegex = r"\w+"
        words = re.findall(wordRegex,sentence)
        for word in words:
            if word.count(targetChar) >= targetQty:
                result.append(word)

print(", ".join(result))