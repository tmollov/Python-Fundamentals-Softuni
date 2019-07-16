class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self,name,age,legs):
        Animal.__init__(self,name,age)
        self.legs = legs
    
    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")
    
    def Print(self):
        print(f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.legs}")

class Cat(Animal):
    def __init__(self,name,age,iq):
        Animal.__init__(self,name,age)
        self.iq = iq
    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")
    
    def Print(self):
        print(f"Cat: {self.name}, Age: {self.age}, IQ: {self.iq}")

class Snake(Animal):
    def __init__(self,name,age,cruelty):
        Animal.__init__(self,name,age)
        self.cruelty = cruelty

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def Print(self):
        print(f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}")
animals = dict()

while True:
    info = input()
    if info == "I'm your Huckleberry":
        break
    
    info = info.split(" ")
    animalType = info[0].lower()
    animalName = info[1]
    if animalType != "talk":   
        animalAge = int(info[2])
        animalSpec = int(info[3])
        if animalType == "dog":
            animals.__setitem__(animalName,Dog(animalName,animalAge,animalSpec))
        elif animalType == "cat":
            animals.__setitem__(animalName,Cat(animalName,animalAge,animalSpec))
        elif animalType == "snake":
            animals.__setitem__(animalName,Snake(animalName,animalAge,animalSpec))
    else:
        animals[animalName].produce_sound()

for animal in animals:
    if hasattr(animals[animal],'legs'):
        animals[animal].Print()

for animal in animals:
    if hasattr(animals[animal],'iq'):
        animals[animal].Print()

for animal in animals:
    if hasattr(animals[animal],'cruelty'):
        animals[animal].Print()