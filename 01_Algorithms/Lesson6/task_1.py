allocated = 0

for new_size in range(1000):
    if allocated < new_size:
        new_allocated = (new_size >> 3) + (3 if new_size < 9 else 6)
        allocated = new_size + new_allocated

    print(f'len = {new_size}\tallocated = {allocated}')

lst = [None] * 10000
print(lst)
lst = []

