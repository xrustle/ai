# 1: Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы.
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import pickle
import json

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]
}

# Записываем, используя pickle
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print('Pickle дамп записан')

# Выводим полученные байты
with open('group.pickle', 'rb') as f:
    result = f.read()
print(result)

# Записываем, используя JSON
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)
print('JSON дамп записан')

# Выводим полученную строку из файла дампа JSON
with open('group.json', 'r') as f:
    result = f.read()
print(result)
