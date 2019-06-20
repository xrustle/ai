import sys

a = [1, 2, 3, 4, 5]
b = a
del a[3] # a.pop(3)
del b
print(sys.getrefcount(a))
print(a)


c = 10000
d = 10100 - 100
print(id(c) == id(d))
print(id(d))

