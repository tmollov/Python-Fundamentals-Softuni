wizards = dict()

while True:
    line = input().split(" ")
    if line[0] == "fight":
        break
    name = line[1]
    health = int(line[2])
    damage = int(line[3])
    if line[0] == "new":
        if wizards.__contains__(name):
            print("Wizard already exists!")
        else:
            wizards.__setitem__(name,[health,damage])
    elif line[0] == "edit":
        if wizards.__contains__(name):
            wizards[name][0] += health
            wizards[name][1] += damage
        else:
              print("Wizard does not exist!")

while True:
    line = input().split(" <=> ")
    if line[0] == "end":
        break

    wizz1 = line[0]
    wizz2 = line[1]
    
    if wizards.__contains__(wizz1) and wizards.__contains__(wizz2):
        wizards[wizz2][0] -= wizards[wizz1][1]
        wizards[wizz1][0] += 50
        if wizards[wizz2][0] <= 0:
            print(f"Fatality - {wizz1} wins!")
            wizards.__delitem__(wizz2)
        else:
            print(f"Next time {wizz2}!")            
    else:
        print("Cannot place a fight with non-existing wizards!")  
        
sor = sorted(wizards.keys(), key=lambda x: wizards[x][0],reverse=True)
for wiz in sor:
    print(f"Wizard: {wiz}. Health: {wizards[wiz][0]}. Damage power: {wizards[wiz][1]}")