class Animal:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("Invalid input!")
        self._name = value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        val = int(value)
        if val <= 0:
            raise ValueError("Invalid input!")
        self._age = val
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self,value):
        value = value.lower()
        if not value or value not in ["male","female"]:
            raise ValueError("Invalid input!")
        self._gender = value
        
    def __str__(self):
        result = f"{self.name} {self.age} {self.gender.capitalize()}"
        return result

class Cat(Animal):
    def __init__(self,name,age,gender):
        Animal.__init__(self,name,age,gender)
    
    def ProduceSound(self):
        return "Meow meow"
    
    def __str__(self):
        newLine = "\n"
        fLine = type(self).__name__
        sLine = super().__str__()
        tLine = self.ProduceSound()
        return f"{fLine}{newLine}{sLine}{newLine}{tLine}"
   
class Dog(Animal):
    def __init__(self,name,age,gender):
        Animal.__init__(self,name,age,gender)
    
    def ProduceSound(self):
        return "Woof!"
    
    def __str__(self):
        newLine = "\n"
        fLine = type(self).__name__
        sLine = super().__str__()
        tLine = self.ProduceSound()
        return f"{fLine}{newLine}{sLine}{newLine}{tLine}" 

class Frog(Animal):
    def __init__(self,name,age,gender):
        Animal.__init__(self,name,age,gender)
    
    def ProduceSound(self):
        return "Ribbit"
    
    def __str__(self):
        newLine = "\n"
        fLine = type(self).__name__
        sLine = super().__str__()
        tLine = self.ProduceSound()
        return f"{fLine}{newLine}{sLine}{newLine}{tLine}"   
   
class Kitten(Animal):
    def __init__(self,name,age,gender):
        Animal.__init__(self,name,age,gender)
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self,value):
        self._gender = "Female"
    
    def ProduceSound(self):
        return "Meow"
    
    def __str__(self):
        newLine = "\n"
        fLine = type(self).__name__
        sLine = super().__str__()
        tLine = self.ProduceSound()
        return f"{fLine}{newLine}{sLine}{newLine}{tLine}"   

class Tomcat(Animal):
    def __init__(self,name,age,gender):
        Animal.__init__(self,name,age,gender)
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self,value):
        self._gender = "Male"
    
    def ProduceSound(self):
        return "MEOW"
    
    def __str__(self):
        newLine = "\n"
        fLine = type(self).__name__
        sLine = super().__str__()
        tLine = self.ProduceSound()
        return f"{fLine}{newLine}{sLine}{newLine}{tLine}" 
 
def factory(classname):
    targetClass = globals()[classname]
    return targetClass
 
while True:
    animalType = input()
    if animalType == "Beast!":
        break

    data = input().split(" ")
    try:
        animal = factory(animalType)(data[0],data[1],data[2])
        print(animal.__str__())
    except ValueError as e:
        print(e.__str__())
    except KeyError:
        print("Invalid input!")