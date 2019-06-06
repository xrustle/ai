# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.

import pickle
import json

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)

print('Словарь, полученный из дампа pickle')
print(my_favourite_group)

with open('group.json', 'r') as f:
    my_favourite_group = json.load(f)

print('Словарь, полученный из дампа JSON')
print(my_favourite_group)
