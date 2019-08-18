functions = {
    "SmartPhone":["make_call","receive_call","send_message","receive_message","browse_internet"],
    "CellPhone":["make_call","receive_call","send_message","receive_message"],
    "Tablet":["stream_movie"]
    }
techs = ["Tablet","CellPhone","SmartPhone"]

class CellPhone():
    def __init__(self,id,os,price):
        self.id = id
        self.os = os
        self.price = price
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        if len(value) < 8 and value.isalpha():
            raise Exception("Invalid id!")
        self._id = value
        
    @property
    def os(self):
        return self._os
    
    @os.setter
    def os(self,value):
        self._os = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value <= 0:
            raise Exception("Invalid price!")
        self._price = value  

    def __str__(self):
        a  = f"Item id: {self.id}\n"
        b = f"Operating system: {self.os}\n"
        c = "Price: %d" % self.price
        return f"{a}{b}{c}"

    def make_call(self):
        print("Making call...")
    
    def receive_call(self):
        print("Receiving a call!")
    
    def send_message(self):
        print("Sending message...")
    
    def receive_message(self):
        print("Receiving a message!")  
    
    def getName(self):
        return type(self).__name__
        
class SmartPhone(CellPhone):
    def __init__(self,id,os,price,apps):
        CellPhone.__init__(self,id,os,price)
        self.apps = apps
    
    @property
    def apps(self):
        return self._apps
    
    @apps.setter
    def apps(self,value):
        if len(value) < 5:
            raise Exception("Invalid number of applications!")
        self._apps = value
    
    def __str__(self):
        p = super().__str__()
        apps = f"\nApplicatons: {', '.join(self.apps)}"
        return p + apps
    
    def browse_internet(self):
        print("Browsing...")
    
    def getName(self):
        return type(self).__name__
    
class Tablet(CellPhone):
    def __init__(self,id,os,price):
        self.id = id
        self.os = os
        self.price = price
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        if len(value) < 8 and value.isalpha():
            raise Exception("Invalid id!")
        self._id = value
        
    @property
    def os(self):
        return self._os
    
    @os.setter
    def os(self,value):
        self._os = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value <= 0:
            raise Exception("Invalid price!")
        self._price = value  

    def __str__(self):
        a  = f"Item id: {self.id}\n"
        b = f"Operating system: {self.os}\n"
        c = "Price: %d" % self.price
        return f"{a}{b}{c}"

    def stream_movie(self):
        print("Streaming movie...")

    def getName(self):
       return type(self).__name__

db = []
while True:
    tech = input().replace("("," ").replace("[","").replace(']',"").replace('"',"").replace(",","").replace(")", "").split(" ")
    
    if tech[0] == "end":
        break
    if tech[0] in ["Phone","Item"]:
        print(f"Can't instantiate abstract class {tech[0]} with abstract methods __init__")
        continue
    try:
        id = tech[1]
        os = tech[2]
        price = float(tech[3])
        gadget = None
        if tech[0] == "Tablet":
            gadget = Tablet(id,os,price)
        elif tech[0] == "CellPhone":
            gadget = CellPhone(id,os,price)
        elif tech[0] == "SmartPhone":
            apps = tech[4:]
            gadget = SmartPhone(id,os,price,apps)
        db.append(gadget)
    except Exception as e:
        print(e.__str__())

while True:
    test = input().split(" ")
    
    if test[0] == "end":
        break

    if test[0] == "report":
        if test[1] not in techs:
            print("Invalid request has been made!")
        else:
            arr = list(filter(lambda x: x.getName() == test[1],db))
            if arr:
                for tech in arr:
                    print(tech)
    elif test[0] == "test":
        id = test[1]
        fun = test[2]
        targets = list(filter(lambda x:x.id == id,db))
        if len(targets) > 0:
            for a in targets:
                tip = a.getName()
                if fun in functions[tip] :
                    getattr(a, fun)()
                else:
                   print("Invalid request has been made!") 
        else:
            print("Invalid request has been made!")