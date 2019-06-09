# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# ----------------------------------------------------------------------------------------------------------------------
# Я выбрал задачу №7 из домашнего задания к уроку 3 (Массивы. Кортежи. Множества. Списки.)
#   В одномерном массиве целых чисел определить два наименьших элемента.
#   Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# РЕЗУЛЬТАТЫ в конце модуля

from timeit import timeit
from random import randint
# Ниже подключение модуля twominscpp, который я написал на C++, для решения этой задачи, но можно
# запустить и без него, тогда будут проверяться только 3 алгоритма Python из этого файла.
CPP_IMPORTED = False
try:
    from twominscpp import solution4
    CPP_IMPORTED = True
except ModuleNotFoundError:
    print('Необходимо установить модуль с помощью <python setup.py install> из папки CPPModule, либо <py -m pip install .>')


# 1. Мое решение задачи из ДЗ
def solution1(array):
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
def solution2(array):
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i
    return array[min_first], array[min_second]


# 3. Пример из разбора ДЗ 2
def solution3(array):
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    return min_1, min_2


# ----------------------------------------------------------------------------------------------------------------------
# Тестирование времени выполнения
def test(func_list, values):
    for i in values:
        array = [randint(-1000, 1000) for i in range(i)]
        for func in func_list:
            test_array = array.copy()  # копирую список, потому что 3-й метод изменяет список
            time = timeit('func(var)', number=100, globals={'func': func, 'var': test_array})
            print(f'{func.__name__}({i}): {time:.6f}')


# Список проверяемых алгоритмов
funcs = [solution1, solution2, solution3]

# 4. В список проверяемых алгоритмов добавляем метод из модуля, написанного на C++, при условии,
# что модуль успешно подключился
if CPP_IMPORTED:
    funcs.append(solution4)

# Входные данные для проверки [5K, 10K, 20K ... - длины списков
rng = [2 ** i * 5000 for i in range(5)]


test(funcs, rng)


# ----------------------------------------------------------------------------------------------------------------------
# РЕЗУЛЬТАТЫ

# solution1(5000): 0.066813
# solution2(5000): 0.108213
# solution3(5000): 0.028061
# solution4(5000): 0.008197
# solution1(10000): 0.179668
# solution2(10000): 0.243169
# solution3(10000): 0.055955
# solution4(10000): 0.016117
# solution1(20000): 0.267227
# solution2(20000): 0.404253
# solution3(20000): 0.113168
# solution4(20000): 0.031986
# solution1(40000): 0.532687
# solution2(40000): 0.806809
# solution3(40000): 0.224670
# solution4(40000): 0.064093
# solution1(80000): 1.087782
# solution2(80000): 1.530153
# solution3(80000): 0.453038
# solution4(80000): 0.128654

# ВЫВОД
# Скорость работы всех алгоритмов с ростом числа элементов массива растет ~линейно.
# Можно оценить сложность как O(n), так как во всех методах мы перебираем полный набор чисел из массива n.
# Но скорости отличаются в константу раз из-за разного количества операций при полном проходе по числам массива

# Лучшим алгоритмом естественно оказался №4 из модуля С++
