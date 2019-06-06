# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом,
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# ----------------------------------------------------------------------------------------------------------------------
# Я выбрал задачу №7 из домашнего задания к уроку 3 (Массивы. Кортежи. Множества. Списки.)
#   В одномерном массиве целых чисел определить два наименьших элемента.
#   Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# В качестве тестовых данных использовал:
# a) массив случайных чисел 5K, 10K и 20K эдементов
# b) также пробовал массив из чисел по порядку от 0 до 5K, от 0 до 10К и от 0 до 20К
# с) и обратную последовательность чисел. Также три варианта.

# РЕЗУЛЬТАТЫ в конце модуля

from random import randint

# a)
# array = [randint(-1000, 1000) for i in range(5000)]
array = [randint(-1000, 1000) for i in range(10000)]
# array = [randint(-1000, 1000) for i in range(20000)]

# b)
# array = [i for i in range(5000)]
# array = [i for i in range(10000)]
# array = [i for i in range(20000)]

# c)
# array = [i for i in range(5000, -1, -1)]
# array = [i for i in range(10000, -1, -1)]
# array = [i for i in range(20000, -1, -1)]


# 1. Мое решение задачи из ДЗ
def solution1():
    a = array[0]
    b = array[1]
    if a > b:
        a, b = b, a

    for i in range(2, len(array)):
        if array[i] < a:
            b = a
            a = array[i]
        elif array[i] < b:
            b = array[i]
    return a, b


# 2. Пример из разбора ДЗ 1
def solution2():
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

    for i in range(3, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i
    return array[min_first], array[min_second]


# 3. Пример из разбора ДЗ 2
def solution3():
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    return min_1, min_2


# ----------------------------------------------------------------------------------------------------------------------
# РЕЗУЛЬТАТЫ

# a) Случайные числа
# solution 1, 5K чисел: 100 loops, best of 5: 562 usec per loop
# solution 2, 5K чисел: 100 loops, best of 5: 759 usec per loop
# solution 3, 5K чисел: 100 loops, best of 5: 203 usec per loop
# solution 1, 10K чисел: 100 loops, best of 5: 1.14 msec per loop
# solution 2, 10K чисел: 100 loops, best of 5: 1.53 msec per loop
# solution 3, 10K чисел: 100 loops, best of 5: 440 usec per loop
# solution 1, 20K чисел: 100 loops, best of 5: 2.29 msec per loop
# solution 2, 20K чисел: 100 loops, best of 5: 3.16 msec per loop
# solution 3, 20K чисел: 100 loops, best of 5: 887 usec per loop

# b) Возрастающая последовательность целых чисел по порядку от нуля
# solution 1, 5K чисел: 100 loops, best of 5: 468 usec per loop
# solution 2, 5K чисел: 100 loops, best of 5: 717 usec per loop
# solution 3, 5K чисел: 100 loops, best of 5: 147 usec per loop
# solution 1, 10K чисел: 100 loops, best of 5: 949 usec per loop
# solution 2, 10K чисел: 100 loops, best of 5: 1.39 msec per loop
# solution 3, 10K чисел: 100 loops, best of 5: 308 usec per loop
# solution 1, 20K чисел: 100 loops, best of 5: 1.95 msec per loop
# solution 2, 20K чисел: 100 loops, best of 5: 2.72 msec per loop
# solution 3, 20K чисел: 100 loops, best of 5: 630 usec per loop

# c) Убывающая последовательность целых чисел по порядку до нуля
# solution 1, 5K чисел: 100 loops, best of 5: 445 usec per loop
# solution 2, 5K чисел: 100 loops, best of 5: 761 usec per loop
# solution 3, 5K чисел: 100 loops, best of 5: 207 usec per loop
# solution 1, 10K чисел: 100 loops, best of 5: 880 usec per loop
# solution 2, 10K чисел: 100 loops, best of 5: 1.54 msec per loop
# solution 3, 10K чисел: 100 loops, best of 5: 435 usec per loop
# solution 1, 20K чисел: 100 loops, best of 5: 1.76 msec per loop
# solution 2, 20K чисел: 100 loops, best of 5: 3.09 msec per loop
# solution 3, 20K чисел: 100 loops, best of 5: 891 usec per loop

# ВЫВОД
# Скорость работы всех трех алгоритмов с ростом числа элементов массива растет практически линейно.
# Можно грубо оценить сложность как O(n).
#
# А лучшим алгоритмом оказался №3 с использвоанием стандартной функции min и метода remove. Этого я не ожидал...
