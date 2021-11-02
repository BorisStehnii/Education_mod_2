import time


def write_logs(func):

    def write_args(*args):

        with open(f"{func.__name__}.log", "a") as file:
            time_start = time.time()
            result = func(*args)
            time_end = time.time()
            string_ = f"Func:{func.__name__}; time start:{time_start}; working time:{time_end - time_start}; " \
                      f"result: {result}\n"
            file.write(string_)
    return write_args


@write_logs
def func_test(x: int, y):
    if not isinstance(x, int):
        raise TypeError
    return sum(x_1**y for x_1 in list(range(x)))


@write_logs
def func_test_2(x: int, y):
    if not isinstance(x, int):
        raise TypeError
    return sum(x_1**y for x_1 in list(range(x)))


func_test(4555504, 2)
func_test_2(24555.4, 4)
