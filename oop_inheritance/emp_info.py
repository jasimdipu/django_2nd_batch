from employee import Employee


class Emp_info(Employee):

    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    def getempname(self):
        return self.__name

    def getempdept(self):
        return self.__dept

    def __str__(self):
        return self.__name+" "+self.__dept
