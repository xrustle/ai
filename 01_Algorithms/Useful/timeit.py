import timeit


# пример функции, которую хотим исследрвать
def sqr(num):
    res = num ** 2
    return res


# вводим данные и проверяем работоспособность
a = int(input('Какое число возвести в квадрат: '))
print(sqr(a))

# такой вариант выдаёт ошибку
print(timeit.timeit('sqr(a)', number=100))

# правильный подход - передать словарь с необходимыми для тестирования объектами
print(timeit.timeit('sqr_for_test(my_number)', number=1000, globals={'sqr_for_test': sqr, 'my_number': a}))

# правильный подход на скорую руку - передать всё глобальное окружение
print(timeit.timeit('sqr(a)', number=10000, globals=globals()))
