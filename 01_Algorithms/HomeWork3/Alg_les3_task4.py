# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 100
lst = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(lst)

s = set()  # Сюда буду складывать все различные числа встречающиеся в массиве, чтобы потом сравнивать с ним

max_n = lst[0]
max_c = 1
for i in range(0, len(lst) - 1):
    n = lst[i]
    counter = 1  # Счетчик числа вхождений числа
    if n in s:
        continue
    for j in range(i + 1, len(lst)):
        if lst[j] == n:
            counter += 1
    if counter > max_c:
        max_c = counter
        max_n = n
    s.add(n)

print(max_c)
print(max_n)
