import math

print(math.pi)


def test1(*a):
    return a


def test2(**b):
    for i in b:
        return i, b[i]


print(test1(1, 2, 3))
print(test2(name="some", age=2))
