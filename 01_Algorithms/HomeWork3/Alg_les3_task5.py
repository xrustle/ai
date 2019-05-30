# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
import math

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
lst = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(lst)

max_neg = -math.inf
for item in lst:
    if 0 > item > max_neg:
        max_neg = item

if max_neg != -math.inf:
    print(f'Максимальный отрицательный элемент: {max_neg}')
else:
    print('В списке нет отрицательных чисел')
