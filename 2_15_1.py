def logger(func):

    def print_func(*args):
        for name_func in globals():
            if name_func in repr(func):
                print(f"{name_func}{args}")
    return print_func


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):

    return [arg ** 2 for arg in args]


add(5, 5)
square_all(2, 5, 10)
