# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# 1 1                        A B 1
# A B 1                      2 C F
# 2 D F                -----------
# -----      AB1 * F =     A 0 5 F
# D 8 0      AB1 * C =     8 0 4 C
#                      -----------
#                        8 A 5 1 F
#            AB1 * 2 = 1 5 6 2
#                      -----------
#                      1 E 0 7 1 F

from collections import deque

HEX = 16
LETTERS = '0123456789ABCDEF'
MAPPING = dict([(LETTERS[i], i) for i in range(len(LETTERS))])


def addition(a, b):
    res = deque()  #результат сложения
    rem = 0  #остаток
    while a or b:
        a_num = MAPPING[a.pop()] if a else 0
        b_num = MAPPING[b.pop()] if b else 0
        res.appendleft(LETTERS[(a_num + b_num + rem) % HEX])
        rem = (a_num + b_num + rem) // HEX
    if rem:
        res.appendleft(LETTERS[rem])
    return res


def multiplication(a, b):
    res = deque()  #результат умножения
    return res


if __name__ == '__main__':
    operator = input('Введите оператор. + или *. Только один символ: ')
    x = deque(input('Введите первое число в 16-тиричной системе: ').upper())
    y = deque(input('Введите второе число в 16-тиричной системе: ').upper())

    if operator == '+':
        r = addition(x, y)
    elif operator == '*':
        r = multiplication(x, y)

    print('Ответ: ', *r, sep='')
