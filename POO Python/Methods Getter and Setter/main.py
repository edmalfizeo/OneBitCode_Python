class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")

    # Method for searching the salary
    def get_salary(self):
        return self.__salary

    # Method for modify the salary
    def set_salary(self, salary):
        self.__salary = salary


charles = Employee("Charles", 1000)
lois = Employee("Lois", 2000)
charles.show()
lois.show()
print(f'Charles Salary: {charles.get_salary()}')
charles.set_salary(1500)
print(f'Charles Salary: {charles.get_salary()}')

