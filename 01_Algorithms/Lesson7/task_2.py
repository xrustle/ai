array = [7, 6, 3, 4, 2, 8, 1, 5, 0, 9]


def selections_sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)

selections_sort(array)
print(array)
