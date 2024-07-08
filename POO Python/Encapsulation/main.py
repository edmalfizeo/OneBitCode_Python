class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")


charles = Employee("Charles", 1000)
lois = Employee("Lois", 2000)
charles.show()
lois.show()
charles.__salary = 1500
charles.show()
