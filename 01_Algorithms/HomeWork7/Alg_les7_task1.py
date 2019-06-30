# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# - алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# - постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные
# версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint

LENGTH = 10
LIMIT = 100


def bubble_sort(arr):
    bubbles = 0
    switch = True

    while switch:
        switch = False
        for i in range(1, len(arr) - bubbles):
            if arr[i - 1] < arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                switch = True
        bubbles += 1
    return arr


if __name__ == '__main__':
    array = [randint(-LIMIT, LIMIT - 1) for _ in range(LENGTH)]  # Целые из [-100, 99] или целые из [-100, 100)
    print(array)
    print(bubble_sort(array))
