import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

pos = int(input('Позиция для вставки: '))
num = int(input('Число для вставки: '))

# array.insert(pos, num)
# print(array)

array.append(None)
print(array)
i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
    print(array)

array[pos] = num
print(array)

array_new = array[:pos] + [num] + array[pos:]
print(array_new)

a, b = (b, a)