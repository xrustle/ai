# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


def merge(name, age, city):
    return f'{name}, {str(age)} года(а), проживает в городе {city}'


print('№1 ', '-' * 100)
print(merge('Василий', 21, 'Москва'))

# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def my_max(n1, n2, n3):
    return max(n1, n2, n3)


print('№2 ', '-' * 100)
print(my_max(4, 25, 3))

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
print('№3 ', '-' * 100)

player = {
    'name': input('Введите имя игрока для задания 3 и 4: '),
    'health': 100,
    'damage': 50
}

enemy = {
    'name': input('Введите имя врага: '),
    'health': 80,
    'damage': 90
}


def attack(attacker, attacked):
    attacked['health'] -= attacker['damage']
    print(attacker['name'], 'атаковал', attacked['name'])


# тест для задания 3
# игрок нападает на врага
attack(player, enemy)
# проверяем сколько здоровья осталось у врага
print('у', enemy['name'], 'осталось', enemy['health'], 'здоровья')

# 4: Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание.
# Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
print('№4 ', '-' * 100)

player['armor'] = 1.2
enemy['armor'] = 1.4


def total_damage(damage, armor):
    return damage / armor


def attack_advanced(attacker, attacked):
    attacked['health'] -= total_damage(attacker['damage'], attacked['armor'])
    print(attacker['name'], 'атаковал', attacked['name'], 'с учетом брони')


# тест для задания 4
# теперь пусть враг нападает на игрока
attack_advanced(enemy, player)
# проверяем сколько здоровья осталось у игрока
print('у', player['name'], 'осталось', player['health'], 'здоровья')
