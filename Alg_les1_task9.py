# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите три различных числа: '))
b = int(input())
c = int(input())

if a > b > c or a < b < c:
    print(f'среднее число {b}')
elif b > a > c or b < a < c:
    print(f'среднее число {a}')
else:
    print(f'среднее число {c}')
