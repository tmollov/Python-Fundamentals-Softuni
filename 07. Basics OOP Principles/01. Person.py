class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        else:
            self._name = name

    @age.setter
    def age(self, age):
        if int(age) < 0:
            raise Exception('Age must be positive!')
        elif int(age) > 180:
            raise Exception('Age must be between 0-180')
        else:
            self._age = age

class Child(Person):
    def __init__(self,name,age):
        Person.__init__(self,name,age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if int(age) < 0:
            raise Exception('Age must be positive!')
        elif int(age) > 15:
            raise Exception("Child's age must be less than 15!")
        else:
            self._age = age
name = input()
age = int(input())

try:
    print(Child(name,age).__str__())
except Exception as e:
    print(str(e))