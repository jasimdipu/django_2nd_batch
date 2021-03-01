# Modules ,Exception Handling & Database Programming
class Exception_Handling:

    def division_by_except(self):
        l = [1, 2, '3', 3, 6, 0, 7, 56]
        try:
            for i in l:
                if i == 0:
                    continue
                elif type(i) == 0:
                    print(100 / i)
                else:
                    print(100 / int(i))
        except Exception as e:
            print(e)

    def another_exception(self, ):

        while True:
            try:
                l = int(input('Enter a number : '))
                print(100 / l)
                break
            except Exception as e:
                print(e)
                self.another_exception()
                break

    def multi_class_exception(self):
        while True:
            try:
                l = int(input('Enter a number : '))
                print(100 / l)
                break
            except ZeroDivisionError as e:
                print(e)
                self.another_exception()
                break
            except ValueError as e:
                print(e)
                self.another_exception()
                break

    def setNumber(self, number):
        try:
            if number > 101:
                raise BigNumberException
            elif number < 0:
                raise SmallNumberException
            print(100 / number)
        except BigNumberException as e:
            print(e)
        except SmallNumberException as e:
            print(e)


# custom exception class

class BigNumberException(Exception):

    def __init__(self, message="The number is bigger then 101"):
        self.message = message
        super().__init__(self.message)


class SmallNumberException(Exception):
    def __init__(self, message="The number is smaller then 0"):
        self.message = message
        super().__init__(self.message)


ex = Exception_Handling()
ex.setNumber(-19)
