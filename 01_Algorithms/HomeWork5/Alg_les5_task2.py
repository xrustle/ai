# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

HEX = 16
LETTERS = '0123456789ABCDEF'
MAPPING = dict([(LETTERS[i], i) for i in range(len(LETTERS))])


# Функция сложения двух 16-еричных чисел. На вход строки или deque. Вывод в deque
def hex_addition(a_str, b_str):
    a = deque(a_str)
    b = deque(b_str)
    res = deque()  #результат сложения
    rem = 0  #остаток
    while a or b:
        a_num = MAPPING[a.pop()] if a else 0
        b_num = MAPPING[b.pop()] if b else 0

        temp = a_num + b_num + rem
        res.appendleft(LETTERS[temp % HEX])
        rem = temp // HEX
    if rem:
        res.appendleft(LETTERS[rem])
    return res


# Функция умножения 16-еричного числа на 16-чную "цифру"
def hex_digit_mul(a_str, digit):
    a = deque(a_str)
    res = deque()  #результат сложения
    rem = 0  #остаток
    while a:
        a_num = MAPPING[a.pop()]

        temp = a_num * digit + rem
        res.appendleft(LETTERS[temp % HEX])
        rem = temp // HEX
    if rem:
        res.appendleft(LETTERS[rem])
    return res


# Функция умножения двух 16-еричных чисел. На вход строки или deque. Вывод в deque
def hex_multiplication(a_str, b_str):
    a = deque(a_str)
    res = '0'  #результат умножения
    for i, item in enumerate(reversed(a)):
        res = hex_addition(hex_digit_mul(b_str, MAPPING[item]) + deque('0' * i), res)
    return res


if __name__ == '__main__':
    operator = None
    while operator not in ['*', '+']:
        operator = input('Введите оператор. + или *. Только один символ: ')

    x = input('Введите первое число в 16-тиричной системе: ').upper()
    y = input('Введите второе число в 16-тиричной системе: ').upper()

    if operator == '+':
        r = hex_addition(x, y)
    else:
        r = hex_multiplication(x, y)

    print(f'{x} {operator} {y} = ', end='')
    print(*r, sep='')
