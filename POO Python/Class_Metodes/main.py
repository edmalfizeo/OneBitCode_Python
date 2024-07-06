"""
1 - Class Metode can use the parameters of the class
2 - Class Metode can acess or modify the class state
3 - We use the decorator @classmethod for define a class metode
"""

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls, text):
        import re
        item = re.findall(r'the \w*', text)
        name = item[0][4:]
        item2 = re.findall(r'is \w*', text)
        price = item2[0][3:]
        return cls(name, int(price))


ps5 = Console.from_text('The price of the PS5 is 500$')
xbox = Console.from_text('The price of the Xbox is 300$')
print(ps5.__dict__)
print(xbox.__dict__)
