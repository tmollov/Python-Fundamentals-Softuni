class BankAccount:
    def __init__(self,name,accName,balance):
        self.name = name
        self.accName = accName
        self.balance = balance

    def Print(self):
        print(f"{self.accName} -> {self.balance:.2f} ({self.name})")
data = []

while True:
    line = input().split(" | ")
    if len(line) == 1:
        break
    data.append(BankAccount(line[0],line[1],float(line[2])))

data = sorted(data, key=lambda x: len(x.name)) 
data = sorted(data, key=lambda x: x.balance,reverse=True) 
for el in data:
    el.Print()