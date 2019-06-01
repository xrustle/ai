# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_X = 5
SIZE_Y = 5
MIN_ITEM = 10
MAX_ITEM = 99

m = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
for line in m:
    print(line)

max_min = MIN_ITEM
for i in range(SIZE_X):
    local_min = m[0][i]
    for j in range(SIZE_Y):
        if m[j][i] < local_min:
            local_min = m[j][i]
    if local_min > max_min:
        max_min = local_min

print(f'\nОтвет: {max_min}')
