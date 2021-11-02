import time


def write_logs(name_log_file):

    def write_func(func):

        def write_args(*args):

            with open(name_log_file, "a") as file:
                time_start = time.time()
                result = func(*args)
                time_end = time.time()
                string_ = f"Func:{func.__name__}; time start:{time_start}; working time:{time_end - time_start}; " \
                          f"result: {result}\n"
                file.write(string_)
        return write_args
    return write_func


@write_logs("logs.log")
def funk_test(x, y):
    if not isinstance(x, int):
        raise TypeError
    return sum(x_1**y for x_1 in list(range(x)))


funk_test(4555504, 2)
