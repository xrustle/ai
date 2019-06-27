def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой'

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]  # O(n**(4/3)) - уточнить в гугле
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()  # yield == return

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                print(array)


array = [7, 6, 3, 4, 2, 8, 1, 5, 0, 9]
shell_sort(array)
print(array)
