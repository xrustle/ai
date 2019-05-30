# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_X = 4
SIZE_Y = 7
MIN_ITEM = 10
MAX_ITEM = 99
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
for line in matrix:
    print(line)

