# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите трехзначное число: '))

s = n // 100 + n % 100 // 10 + n % 10
prod = (n // 100) * (n % 100 // 10) * (n % 10)

print(f'Сумма цифр = {s}')
print(f'Произведение цифр = {prod}')
