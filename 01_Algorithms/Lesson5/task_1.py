from collections import Counter


a = Counter()
b = Counter('arbakadabra')
c = Counter({'dogs': 5, 'cats': 13})
d = Counter(dogs=5, cats=13)

print(a, b, c, d, sep='\n')

print(b['z'])
b['z'] = 3
print(b)
print(type(b))

print(b.most_common(3))
print(list(b.elements()))

x = Counter(a=3, b=-2, c=2, d=5, z=5)
y = Counter(a=2, b=1, c=-1, d=3)
print(x, y)
print(x + y)
print(x - y)
print(x & y)
print(x | y)


