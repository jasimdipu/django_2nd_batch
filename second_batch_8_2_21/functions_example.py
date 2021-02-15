# functions
# print("Welcome to python")


# function declaration

def greetings():
    print("Welcome Naim")


# function with parameters
def greetings_with_name(name):
    print("Welcome ", name)


def getEmpSalary(name):
    salary = {
        'Emon': 1200,
        'Salam': 12323,
        'Rofiq': 3432
    }
    for i in salary.keys():
        if i == name:
            print(salary[i])
            break
    else:
        print("No Data")


def getBiggerNumber(a, b):
    if a > b:
        return a
    else:
        return b


l = [1, -2, 4, -6, 3, 5, -7, 7, -5, 30]


def countNegPos(l):
    c = 0
    a = 0
    for i in l:
        if i >= 0:
            c += 1
        else:
            a += 1
    print(c)
    print(a)

greetings()
greetings_with_name("Akram")
greetings_with_name("Lokman")

getEmpSalary('Emon')

print(getBiggerNumber(10, 20))
countNegPos([1, -2, 4, -6, 3, 5, -7, 7, -5, 30])

# salary = {
#     'Emon': 1200,
#     'Salam': 12323,
#     'Rofiq': 3432
# }
#
# print(salary.keys())
