import time
from functools import wraps


def log(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        with open('log.txt', 'a') as file:
            file.write(f'{time.ctime(time.time())}: started <{f.__name__}> with result {result}\n')
        return result
    return wrapper


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print('Время выполнения функции %f' % delta_time)
        return result
    return wrapper
