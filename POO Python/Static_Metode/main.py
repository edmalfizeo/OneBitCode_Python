"""
1 - The Static Method doesn't use class parameters
2 - The Static Method can acess but not modify the class attributes
3 - Use the decorator @staticmethod to define a static method
"""

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def course_trail(trail):
        if trail == 'Python Foundation':
            cousers = ['Python Basic', 'Python Intermediate', 'Python Advanced']
        elif trail == 'Java Foundation':
            cousers = ['Java Basic', 'Java Intermediate', 'Java Advanced']
        else:
            cousers = ['Course not found']
        return cousers


print(Course.course_trail('Python Foundation'))
print(Course.course_trail('Data Analises'))
