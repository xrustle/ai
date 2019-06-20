import sys

sys.setrecursionlimit(10000)

def akk(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


a = int(input('a = '))
b = int(input('b = '))
res = akk(a, b)
print(res)
