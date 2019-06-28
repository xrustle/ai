# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random

LENGTH = 10
LIMIT = 50


def merge(arr, left, right):
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[l + r] = left[l]
            l += 1
        else:
            arr[l + r] = right[r]
            r += 1

    for l in range(l, len(left)):
        arr[l + r] = left[l]

    for r in range(r, len(right)):
        arr[l + r] = right[r]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    merge(arr, left_arr, right_arr)
    return arr


if __name__ == '__main__':
    array = [random() * LIMIT for _ in range(LENGTH)]  # Вещественные из [0, 50)
    print(array)
    print(merge_sort(array))
