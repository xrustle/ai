import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_folder
from game import play

save_info('Начало')
command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла или папки')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Не хватает параметров')
        print('Должно быть 2 параметра: имя исходного файла ила папки и имя нового файла или папки')
    else:
        copy_file(name, new_name)
elif command == 'chdir':
    try:
        path = sys.argv[2]
    except IndexError:
        print('Отсутствует путь')
    else:
        change_folder(path)
elif command == 'play':
    play()
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('chdir - смена рабочей директории')

save_info('Конец')
