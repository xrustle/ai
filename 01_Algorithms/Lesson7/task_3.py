import random


def quick_sort(array, fst, lst):
    # print(array)
    if fst >= lst:
        return
    pivot = array[random.randint(fst, lst)]
    i = fst
    j = lst

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quick_sort(array, fst, j)
    quick_sort(array, i, lst)


array = [7, 6, 3, 4, 2, 8, 1, 5, 0, 9]
quick_sort(array, 0, len(array) - 1)
print(array)
