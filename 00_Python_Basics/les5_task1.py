# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
import os


def create_dirs():
    for i in range(1, 2):
        os.mkdir(f'dir_{i}')


def remove_dirs():
    for i in range(1, 2):
        os.rmdir(f'dir_{i}')


if __name__ == '__main__':
   # create_dirs()
    remove_dirs()
