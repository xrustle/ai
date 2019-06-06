# python -m timeit -n 100 -s "import task_4" "task_4.fib(10)"
import cProfile
import functools

# 1. Рекурсия
@functools.lru_cache(maxsize=25) # не для практического задания к уроку
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# "task_4.fib(10)"
# 100 loops, best of 3: 18.2*10**-6 usec per loop
# "task_4.fib(15)"
# 100 loops, best of 3: 224 usec per loop
# "task_4.fib(20)"
# 100 loops, best of 3: 2.63 msec per loop
# cProfile.run('fib(20)')
# 177/1    0.000    0.000    0.000    0.000 task_4.py:5(fib)  - 10
# 21891/1    0.005    0.000    0.005    0.005 task_4.py:5(fib)    - 20

# 2. Рекурсия + словарь
def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

# "task_4.fib_dict(10)"
# 100 loops, best of 3: 3.66 usec per loop
#  "task_4.fib_dict(20)"
# 100 loops, best of 3: 6.91 usec per loop
# "task_4.fib_dict(40)"
# 100 loops, best of 3: 14 usec per loop
# cProfile.run('fib_dict(20)')
# 19/1    0.000    0.000    0.000    0.000 task_4.py:24(_fib_dict) - 10
# 39/1    0.000    0.000    0.000    0.000 task_4.py:24(_fib_dict) - 20

# 3. Цикл
def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second

# "task_4.fib_loop(10)"
# 100 loops, best of 3: 0.711 usec per loop
#  "task_4.fib_loop(100)"
# 100 loops, best of 3: 9.05 usec per loop
#  "task_4.fib_loop(1000)"
# 100 loops, best of 3: 70.8 usec per loop
# cProfile.run('fib_loop(100)')
# 1    0.000    0.000    0.000    0.000 task_4.py:43(fib_loop)

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# test_fib(fib)
# test_fib(fib_dict)
# test_fib(fib_loop)


