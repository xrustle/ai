# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
lst = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(lst)

a = lst[0]
b = lst[1]
if a > b:
    a, b = b, a

for i in range(2, len(lst)):
    if lst[i] < a:
        b = a
        a = lst[i]
    elif lst[i] < b:
        b = lst[i]

print(f'Два наименьших числа {a} и {b}')
