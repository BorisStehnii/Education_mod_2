from functools import wraps


def logger(func):
    @wraps(func)
    def print_func(*args):
        args = " ".join(map(str, args))
        print(f"{func.__name__} {args}")
    return print_func


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):

    return [arg ** 2 for arg in args]


add(5, 5)
square_all(1, 3, 5)
