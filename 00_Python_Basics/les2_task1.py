# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# Примечание. Списки создайте вручную, например так:

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

new_list = []
for number in my_list_1:
    if number not in my_list_2:
        new_list.append(number)

my_list1 = new_list
print(f'Ответ: {new_list}')
