class Student:
    # attributes(attr), constructors, functions
    # attr -> Global variable/instance/class properties
    name = ''
    age = 0
    dept = ''

    # constructor -> function
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def get_name(self):
        return self.name

    def set_name(self, name):
        print(name)
        # self.name = name

    def __str__(self):
        return "Student name: {}\nStudent age: {}\nStudent department: {}".format(self.name, self.age, self.dept)


# object create
student = Student("Abir", 21, "CSE")
print(student)
print(student.get_name())
student.set_name('hasan')
print(student.get_name())
