array = [7, 6, 3, 4, 2, 8, 1, 5, 0, 9]

# сортировка пузырьком
n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)

print(array)
