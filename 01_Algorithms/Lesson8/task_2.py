h_list = [None] * 26


def my_append(value):
    my_hash = ord(value[0]) - ord('a')
    h_list[my_hash] = value
    print(h_list)


a = 'apple'
my_append(a)

b = 'banana'
my_append(b)

c = 'ananas'
my_append(c)

print(4567 == 4 * 10 ** 3 + 5 * 10 ** 2 + 6 * 10 ** 1 + 7 * 10 ** 0)


def my_index(value):
    letter = 26
    my_hash = 0
    SIZE = 10000
    for i, char in enumerate(value):
        my_hash += (ord(char) - ord('a') + 1) * letter ** i
    return my_hash % SIZE


print(my_index(a))
print(my_index(b))
print(my_index(c))
