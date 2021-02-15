# Iterator
# built in function which return value on continuous process called iterator
print(range(10))
print(list(range(10)))


# Generator
# Custom function which return value on continuous process called generator
def my_range(n):
    for i in range(n):
        yield i


print(list(my_range(20)))

for i in my_range(10):
    print(i)

# next
i = iter("aihfasu")
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


# map
def getnum(a, b):
    return a+b

# 1+2+3+4+...+n = ?


print(list(map(getnum, [1, 2, 3, 4, 5], [1, 2, 3, 4, 15])))
# print(getnum([1, 2, 3, 4, 5]))