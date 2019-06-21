import sys
from random import randint
from collections import deque

print(sys.version)   # 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
print('*' * 50)


# Функция подсчета выделенной памяти
def getfullsizeof(var):
    mem = sys.getsizeof(var)
    if hasattr(var, '__iter__'):
        if hasattr(var, 'items'):
            for item in var.items():
                mem += getfullsizeof(item)
        else:
            for item in var:
                if item is not var:
                    mem += getfullsizeof(item)
    return mem


# Считает сумму выделенной памяти по всем переменных словаря vars
# Эту функцию помещу в конец исследуемых функций
def mem_usage(locs):
    mem = 0
    for value in locs.values():
        mem += getfullsizeof(value)
    return mem


# 1. Поиск двух минимальных элементов в массиве
#    Используется 18338786 байт при работе с массивом в 1 млн элементов
def two_mins():
    array = [randint(-100, 100) for i in range(1000000)]

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

    print(mem_usage(locals()))  # Подсчет памяти
    return a, b


# 2. Поиск максимального элемента среди минимальных элементов в столбцам матрицы
#    Используется 18520628 байт при работе с матрицей в 1000x1000
#    Примерно как в предыдущей функции, потому что элементов для хранения также 1 млн
def max_in_mins():
    size_x = 1000
    size_y = 1000
    min_item = 10
    max_item = 99

    m = [[randint(min_item, max_item) for _ in range(size_x)] for _ in range(size_y)]

    max_min = None
    for i in range(len(m[0])):
        local_min = m[0][i]
        for j in range(len(m)):
            if m[j][i] < local_min:
                local_min = m[j][i]
        if max_min is None or local_min > max_min:
            max_min = local_min

    print(mem_usage(locals()))  # Подсчет памяти
    return max_min


# 3. Сложение шестнадцетиричных чисел
# Используется 605045 байт при сложении двух чисел длиной 10000 знаков
# В этой функции считал память после инициализации и определения двух очередей.
# Далее размер памяти будет уменьшаться, так как из обеих очередей забираем с конца элементы методом pop()
def hex_addition():
    base = 16
    letters = '0123456789ABCDEF'
    mapping = dict([(letters[i], i) for i in range(len(letters))])

    a = deque([letters[randint(0, 15)] for _ in range(10000)])
    b = deque([letters[randint(0, 15)] for _ in range(10000)])

    print(mem_usage(locals()))  # Подсчет памяти

    res = deque()
    rem = 0
    while a or b:
        a_num = mapping[a.pop()] if a else 0
        b_num = mapping[b.pop()] if b else 0

        temp = a_num + b_num + rem
        res.appendleft(letters[temp % base])
        rem = temp // base
    if rem:
        res.appendleft(letters[rem])

    return res


funcs = [two_mins, max_in_mins, hex_addition]
for func in funcs:
    print(func.__name__, end=': ')
    func()

# OUTPUT
# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
# **************************************************
# two_mins: 18338786
# max_in_mins: 18520628
# hex_addition: 605045
