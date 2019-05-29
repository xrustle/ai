a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7]
print(a, b, sep='\n')

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7]  # a.extend([5, 6, 7])
print(a, b, sep='\n')

# 2.
row = [' '] * 3
print(row)
board = [row] * 3
print(board)
board[0][0] = 'X'
print(board)
board = [[' '] * 3 for _ in range(3)]
board[0][0] = 'X'
print(board)

# 3.
set_x = {1, 2}
lst_x = [3, 4]
dict_x = {tuple(lst_x): set_x}
print(dict_x)
dict_y = {frozenset(set_x): lst_x}
print(dict_y)
