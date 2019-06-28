# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)

from random import randint

M = 5  # Длина массива в примере равна 2 * M + 1


def get_item(array, position):
    if len(array) == 1:
        return array[0]

    pivot = array[len(array) // 2]  # Можно существенно улучшить алгоритм, если искать опорный элемент по-умному)

    greater = [item for item in array if item > pivot]
    equal = [item for item in array if item == pivot]
    smaller = [item for item in array if item < pivot]

    if position < len(smaller):
        return get_item(smaller, position)
    elif position < len(smaller) + len(equal):
        return equal[0]
    else:
        return get_item(greater, position - len(equal) - len(smaller))


def median(array):
    if len(array) % 2:
        return get_item(array, len(array) / 2)
    else:
        raise ValueError('Функция median только для списков нечетной длины')


if __name__ == '__main__':
    arr = [randint(0, 100) for _ in range(2 * M)]
    print(arr)
    print(f'Медиана: {median(arr)}')
