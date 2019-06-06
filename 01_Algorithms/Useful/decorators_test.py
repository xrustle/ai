from decorators import log, timer

# my_object = log(my_sum(1, 2, 3))


@log
@timer
def my_sum(x, y):
    return x + y


print(my_sum(1, 2))
