# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
result = 0

for i in range(n):
    result += (-1/2) ** i

print(f'Сумма: {result}')
