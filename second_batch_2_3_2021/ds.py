# list, tuple, set, dictionaries

# list declare

l = [1, 2, 3, 4, 5, 6.5, 7.5, 8.3, 'one', 'two', 'three']  # indexing start = 0, end = n-1

print(l)
print(type(l))
print('-' * 20)
# list single item using indexing
print(l[10])
print('-' * 20)

# collect all items from list
for i in l:
    print(i)
    print(i * 5)
print('-' * 20)

# append data

l.append('four')

print(l)

l.append(['five', 'six'])

print(l)

print(l.index(1))
print("'one' in on ", l.index('one'))
# sort a listed value
sort_list = [2, 4, 3, 1, 4, 2, 5, 45, 93, 43]
print(sort_list)
sort_list.sort()
print(sort_list)

# pop function
p = l.pop()
print(p)
print(l)

p = l.pop(1)
print(p)
print(l)

print(sort_list.count(2))

# nested list

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

l = [l1, l2, l3]
print(l)
print(l[0])
print(l[0][1])

# mutability
l4 = [10, 11, 12]
l.append(l4)
print(l)

lst = [1, 2, 4, 2, 3]
lst[0] = 10
print(lst)

# Tuple
# immutable
t = ()
print(type(t))

t = (1, 2, 3, 4, 5, 6.5, 7.5, 8.3, 'one', 'two', 'three')
print(t)
for i in t:
    print(i, end=' ')

# does not support item assignment t[0] = 10 immutable

t.index(1)

t.count(2)

# set
print()
s = {1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 1, 1, 1, 1}
print(s)
s.add(10)
print(s)

# dictionary
# key value pair
d = {'key1': 10, 'key2': 20, 'key3': 30}
print(d['key1'])
print(d['key2'])

# nested dic
d2 = {'key1': 100, 'key2': 200, 'key3': 300}
dic = {'0': d, '1': d2}
print(dic['1']['key1'])

dic2 = {'key1': {'key1': 1000, 'key2': 2000}, 'key2': [1, 2, 3, 4, 5], 'key3': (1, 2, 3, 4, 5, 6)}
print(dic2['key1'])
print(dic2['key1']['key2'])
print(dic2['key2'][3])

print(dic2.keys())
print(dic2.values())

for i, j in dic2.items():
    if i == 'key2':
        print(i, j)