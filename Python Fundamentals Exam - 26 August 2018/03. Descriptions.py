import re

persons = []

regex = r"name\sis\s([A-z][a-z]+\s[A-z][a-z]*).+\s+([0-9]{2}) years.+on\s(\d{1,2}-\d{1,2}-\d{4})\."
namecheck = r"^[A-Z][a-z]+\s[A-Z][a-z]+$"

while True:
    data= input()
    if len(data) < len("make migrations") or data == "make migrations" :
        break
    else:
        matches = re.findall(regex, data, re.MULTILINE | re.IGNORECASE)
        if matches:
            person = list(matches)
            if not re.match(namecheck,person[0][0]):
                continue
            persons.append([person[0][0],person[0][1],person[0][2]])
            
if persons:
    for i in range (len(persons)):
        print(f"Name of the person: {persons[i][0]}.")
        print(f"Age of the person: {persons[i][1]}.")
        print(f"Birthdate of the person: {persons[i][2]}.")
else:
    print("DB is empty")