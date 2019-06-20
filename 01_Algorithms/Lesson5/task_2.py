from collections import deque

a = deque()
b = deque('abrakadabra')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque('abrakadabra', maxlen=7)
c = deque([1, 2, 3, 4, 5], maxlen=7)
print(b, c, sep='\n')

print('*' * 50)
d = deque([i for i in range(5)])
print(d)
d.append(5)
print(d)
d.appendleft(6)
print(d)
d.extend([7, 8])
print(d)
d.extendleft([9, 10])
print(d)
# d.insert(2, 5)
# print(d)
d.rotate(-2)
print(d)
d.reverse()
print(d)
print(d.pop())
print(d.popleft())


