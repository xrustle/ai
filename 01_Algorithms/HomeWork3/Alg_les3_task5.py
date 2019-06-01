# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
lst = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(lst)

max_neg = MIN_ITEM - 1
max_i = -1
for i, item in enumerate(lst):
    if 0 > item > max_neg:
        max_neg = item
        max_i = i

if max_i != -1:
    print(f'Максимальный отрицательный элемент: {max_neg}. Позиция: {max_i}')
else:
    print('В списке нет отрицательных чисел')
