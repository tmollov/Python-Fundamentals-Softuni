from abc import ABC,abstractmethod
 
 
class Item(ABC):
    @abstractmethod
    def __init__(self, id_n: str, system: str, price: float):
        self.id_n = id_n
        self.system = system
        self.price = price
 
    @property
    def id_n(self):
        return self._id_n
 
    @id_n.setter
    def id_n(self, value):
        if value.isalpha() and len(value) >= 8:
            self._id_n = value
        else:
            raise Exception('Invalid id!')
 
    @property
    def price(self):
        return self._price
 
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise Exception('Invalid price!')
 
    def __str__(self):
        return f'Item id: {self.id_n}\nOperating system: {self.system}\nPrice: {self.price}'
 
 
class Phone(Item):
    @abstractmethod
    def __init__(self, id_n: str, system: str, price: float):
        Item.__init__(self, id_n, system, price)
 
    def make_call(self):
        print('Making call...')
 
    def receive_call(self):
        print('Receiving a call!')
 
    def send_message(self):
        print('Sending message...')
 
    def receive_message(self):
        print('Receiving a message!')
 
 
class SmartPhone(Phone):
    def __init__(self, id_n: str, system: str, price: float, apps: []):
        Phone.__init__(self, id_n, system, price)
        self.apps = apps
 
    @property
    def apps(self):
        return self._apps
 
    @apps.setter
    def apps(self, value):
        if len(value) >= 5:
            self._apps = value
        else:
            raise Exception('Invalid number of applications!')
 
    def browse_internet(self):
        print('Browsing...')
 
    def __str__(self):
        a = f'Item id: {self.id_n}\nOperating system: {self.system}\nPrice: {self.price}'
        b = f"Applications: {','.join(self.apps)}"
        return f'{a}\n{b}'
 
 
class CellPhone(Phone):
    def __init__(self, id_n: str, system: str, price: float):
        Phone.__init__(self, id_n, system, price)
 
 
class Tablet(Item):
    def __init__(self, id_n: str, system: str, price: float):
        Item.__init__(self, id_n, system, price)
 
    def stream_movie(self):
        print('Streaming movie...')
 
 
items = {}
while True:
    data = input()
 
    if data == 'end':
        break
 
    try:
        item = eval(data)
        items[item.id_n] = item
    except Exception as ex:
        print(ex)
 
while True:
    data = input().split()
 
    if data[0] == 'end':
        break
 
    if data[0] == 'test':
        if data[1] in items.keys():
            my_item = items[data[1]]
            my_class = my_item.__class__.__name__
            if data[2] in dir(my_item):
                if my_class == 'Tablet':
                    method = getattr(Tablet, data[2])
                    method(my_item)
                if my_class == 'CellPhone':
                    method = getattr(CellPhone, data[2])
                    method(my_item)
                if my_class == 'SmartPhone':
                    method = getattr(SmartPhone, data[2])
                    method(my_item)
            else:
                print('Invalid request has been made!')
        else:
            print('Invalid request has been made!')
 
    if data[0] == 'report':
        if data[1] == 'Tablet':
            for i in items.values():
                if isinstance(i, Tablet):
                    print(i)
        elif data[1] == 'CellPhone':
            for i in items.values():
                if isinstance(i, CellPhone):
                    print(i)
        elif data[1] == 'SmartPhone':
            for i in items.values():
                if isinstance(i, SmartPhone):
                    print(i)
        else:
            print('Invalid request has been made!')