class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category


class Fish(Animal):
    race = ""


class Parrots(Animal):
    color = ""


class Zoo:
    def __init__(self):
        self.animals_dict = {}

    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category

    def total_of_category(self, category):
        total = 0
        for animal in self.animals_dict.values():
            if animal == category:
                total += 1
        return f"Total of {category}: {total}"


nemo = Fish("Nemo", "Fish")
rio = Parrots("Rio", "Parrots")
zoo = Zoo()
zoo.add_animal(nemo)
zoo.add_animal(rio)
print(zoo.total_of_category("Fish"))
print(zoo.total_of_category("Parrots"))
