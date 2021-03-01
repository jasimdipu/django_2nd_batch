from student_info import Student_info
from emp_info import Emp_info


class Multiple_inheritance(Student_info, Emp_info):

    def __init__(self, name, dept, first_name, last_name):
        super(Student_info, self).__init__(name=name, dept=dept)
        super(Emp_info, self).__init__(first_name=first_name, last_name=last_name, dept=dept)

    def getdept(self):
        return self.getstudept()
