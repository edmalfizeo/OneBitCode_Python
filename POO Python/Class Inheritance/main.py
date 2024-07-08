class Animal:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Lion(Animal):
    mane = True

    def roar(self):
        print(f"{self.name} is roaring")


King_lion = Lion("Mufasa", "Large", "Yellow")
King_lion.eat()
King_lion.roar()
dog = Dog("Rex", "Medium", "Brown")
dog.bark()