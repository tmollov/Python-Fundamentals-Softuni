import re

regex = r"\b(?P<day>\d{2})([-.\/])(?P<mount>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
dates = input()

matches = re.finditer(regex,dates)
for match in matches:
    day = match.group("day")
    mount = match.group("mount")
    year = match.group("year")
    print(f"Day: {day}, Month: {mount}, Year: {year}")