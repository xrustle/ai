# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 99
lst = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(lst)

max_n = lst[0]
min_n = lst[0]
max_i = 0
min_i = 0

for i, n in enumerate(lst):
    if n > max_n:
        max_n = n
        max_i = i
    if n < min_n:
        min_n = n
        min_i = i

lst[max_i], lst[min_i] = lst[min_i], lst[max_i]

print(lst)
