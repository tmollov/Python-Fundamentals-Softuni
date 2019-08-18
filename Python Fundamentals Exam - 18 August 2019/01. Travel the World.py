count = int(input())
price = float(input())

reviews = 0
    
def GetConverted(line):
    digits = []
    for i in range(0,len(line),2):
        digits.append(chr(int(line[i]+line[i+1])))
    return digits
    
for i in range(count):
    line = input()
    if line.isdigit():
        digits = GetConverted(line)
        print(f"Reviewing item - {''.join(digits)}")
        reviews += 1
    elif line.isalpha():
        print(f"Reviewing location - {line[::-1]}")
        reviews += 1
        
print(f"{reviews} reviews have been made this month. Salary: {(reviews*price):.2f}")