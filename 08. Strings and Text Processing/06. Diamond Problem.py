import re
regex = r"<\w+>"
nums = r"[0-9]"
word = input()

matches = re.findall(regex, word, re.MULTILINE | re.IGNORECASE)

if matches:
    for match in matches:
        carats = sum(map(int, re.findall(nums,match)))
        print(f"Found {carats} carat diamond")
else:
    print(f"Better luck next time")    