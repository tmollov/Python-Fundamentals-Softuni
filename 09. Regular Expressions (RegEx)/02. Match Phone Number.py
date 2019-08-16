import re

regex = r"(\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4})\b"
numbers = input()

matches = re.findall(regex,numbers)
for match in matches:
    print(str(match), end=" ")