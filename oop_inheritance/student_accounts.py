from student_info import Student_info  # -> parent class


class StudentAccounts(Student_info):  # child class

    def __init__(self, stu_id, f_name, l_name, dept, subjects, credit, credit_fees, waiver):
        super().__init__(stu_id, f_name, l_name, dept, subjects)
        self.__credit = credit
        self.__credit_fees = credit_fees
        self.__waiver = waiver

    def getSubjectsCount(self):
        totalsubjects = super().getstusubjects()
        count = 0
        for i in totalsubjects:
            count += i

        return count

    def getTotalAmount(self):
        total_amount = self.__credit * self.__credit_fees

        return total_amount

    def gettotalAmountWithWaiver(self):
        withWaiver = self.getTotalAmount() - self.__waiver

        return withWaiver

    def __str__(self):
        return "Student Name: {}\nStudent Dept: {}\n Student Amount: {}\n Student Waiver: {}\n" \
               "Student Total Amount: {}".format(super().getstufname(), super().getstudept(), self.getTotalAmount(),
                                                 self.__waiver, self.gettotalAmountWithWaiver())
