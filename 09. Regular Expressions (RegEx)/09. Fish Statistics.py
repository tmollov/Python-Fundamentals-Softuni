import re  
   
def TailType(length):
    if length > 5:
        return f"Long ({length *2} cm)"
    elif length > 1 and length <= 5:
        return f"Medium ({length *2} cm)"
    elif length == 1:
        return f"Short ({length *2} cm)"
    else:
        return "None"

def BodyType(length):
    if length > 10:
        return f"Long ({length *2} cm)"
    elif length > 5 and length <= 10:
        return f"Medium ({length *2} cm)"
    else:
        return f"Short ({length *2} cm)"

def StatusType(status):
    status = status.lower()
    if status == "'":
        return "Awake"
    elif status == "-":
        return "Asleep"
    elif status == "x":
        return "Dead"

regex = r"((>*)<(\(+)(['|x|-])>)"
fishes = input()
fishCounter = 1

matches = re.findall(regex,fishes)

if not matches:
    print("No fish found.")
    exit()

for match in matches:
    print(f"Fish {fishCounter}: {match[0]}")
    print(f"  Tail type: {TailType(len(match[1]))}")
    print(f"  Body type: {BodyType(len(match[2]))}")
    print(f"  Status: {StatusType(match[3])}")
    fishCounter+=1
