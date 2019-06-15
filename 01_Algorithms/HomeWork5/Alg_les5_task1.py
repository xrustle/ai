# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

QUARTERS = 4

factories = Counter()

for _ in range(int(input('Число предприятий: '))):
    name = input(f'Название предприятия: ')
    for j in range(1, QUARTERS + 1):
        factories[name] += int(input(f'Прибыль {name} в квартале {j}: '))

avg = sum(factories.values()) / len(factories)

print(f'Средняя прибыль за год: {avg}')
print(f'Выше среднего: {[i for i in factories if factories[i] > avg]}')
print(f'Ниже среднего: {[i for i in factories if factories[i] < avg]}')
