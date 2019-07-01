name = input()
age = int(input())
town = input()
salary = float(input())
ageRange = ""
salaryRange = ""
if age < 18:
    ageRange = "teen"
elif age < 70:
    ageRange = "adult"
else:
    ageRange = "elder"

if salary < 500:
    salaryRange = "low"
elif age < 2000:
    salaryRange = "medium"
else:
    salaryRange = "high"


print(f"Name: {name}")
print(f"Age: {age}")
print(f"Town: {town}")
print(f"Salary: ${salary:.2f}")
print(f"Age range: {ageRange}")
print(f"Salary range: {salaryRange}")