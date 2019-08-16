import re
class Human:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self,value):
        if value == value.capitalize():
            if len(value) >= 4:
                self._firstName = value
            else:
                raise Exception("Expected length at least 4 symbols! Argument: firstName") 
        else:
            raise Exception("Expected upper case letter! Argument: firstName")
       
    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self,value):
        if value == value.capitalize():
            if len(value) >= 3:
                self._lastName = value
            else:
                raise Exception("Expected length at least 3 symbols! Argument: lastName") 
        else:
            raise Exception("Expected upper case letter! Argument: lastName")
    
    def __str__(self):
        newLine = "\n"
        fName = f"First Name: {self.firstName}{newLine}"
        lName = f"Last Name: {self.lastName}{newLine}"
        return f"{fName}{lName}"

class Student(Human):
    def __init__(self,fname,lname,facultyNum):
        Human.__init__(self,fname,lname)
        self.facultyNumber = facultyNum
        
    @property
    def facultyNumber(self):
        return self._facultyNumber

    @facultyNumber.setter
    def facultyNumber(self,value):
        pattern = re.compile(r"^\w{5,10}$")
        pattern.match(value)
        if pattern.match(value):
            self._facultyNumber = value
        else:
            raise Exception("Invalid faculty number!")
    
    def __str__(self):
        newLine = "\n"
        fNumber = f"Faculty number: {self.facultyNumber}{newLine}"    
        result = f"{super().__str__()}{fNumber}"
        return result
    
class Worker(Human):
    def __init__(self,fname,lname,weekSalary,workHoursPerDay):
        Human.__init__(self,fname,lname)
        self.weekSalary = weekSalary
        self.workHoursPerDay = workHoursPerDay
    
    @property
    def weekSalary(self):
        return self._weekSalary
    
    @weekSalary.setter
    def weekSalary(self,value):
        val = float(value)
        if val <= 10.0 :
            raise Exception("Expected value mismatch! Argument: weekSalary")
        self._weekSalary = val
    
    @property
    def workHoursPerDay(self):
        return self._workHoursPerDay
    
    @workHoursPerDay.setter
    def workHoursPerDay(self,value):
        value = float(value)
        if value >= 1 and value <= 12:
            self._workHoursPerDay = value
        else:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")
    
    def __str__(self):
        newLine = "\n"
        main = super().__str__()
        salary = f"Week Salary: {self.weekSalary:.2f}{newLine}"
        day = f"Hours per day: {self.workHoursPerDay:.2f}{newLine}"
        salaryPerHour = self.weekSalary / (5 * self.workHoursPerDay)
        hour = f"Salary per hour: {salaryPerHour:.2f}"
        return f"{main}{salary}{day}{hour}"
        
try:
    f = input().split()
    s = input().split()
    a = Student(f[0],f[1],f[2])
    b = Worker(s[0],s[1],s[2],s[3])
    print(a)
    print(b)
except Exception as e:
    print(str(e))