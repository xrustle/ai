def func(a, b):
    """
    func(1, 5)
    '1, 2, 3, 4, 5'
    func(5, 5)
    '5'
    """
    if a == b:
        return f'{a}'

    if a < b:
        return f'{a}, {func(a + 1, b)}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'


print(func(10, 5))
