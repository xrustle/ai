# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# Примечание. Списки создайте вручную, например так:

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

# В этом случае ответ будет:
# [5, 8]

new_list = []

for i, item in enumerate(my_list_1):
    for j, item2 in enumerate(my_list_1):
        if item == item2 and i != j:
            break
    else:
        new_list.append(item)

print(new_list)
