# inheritance

from student import Student

class Student_info(Student):

    # encapsulation-> 1. private(__), 2.protected(_), 3.public

    # constructor
    def __init__(self, stu_id, f_name, l_name, dept, subjects):
        self.__stu_id = stu_id
        self.__f_name = f_name
        self.__l_name = l_name
        self.__dept = dept
        self.__subjects = subjects

    def getstudentid(self):
        return self.__stu_id

    def getstufname(self):
        return self.__f_name

    def getstulname(self):
        return self.__l_name

    def getstudept(self):
        return self.__dept

    def getstusubjects(self):
        return self.__subjects



