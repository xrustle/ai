# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
lst = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(lst)

result = []
for i, n in enumerate(lst):
    if n % 2 == 0:
        result.append(i)

print(result)
