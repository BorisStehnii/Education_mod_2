import time


def write_logs(func):

        def write_args(*args):

            args_name = "_".join(map(str, args))
            with open(f"{func.__name__}_{args_name}.log", "a") as file:
                time_start = time.time()
                result = func(*args)
                time_end = time.time()
                string_ = f"Func:{func.__name__}; time start:{time_start}; working time:{time_end - time_start}; " \
                          f"result: {result}\n"
                file.write(string_)
        return write_args


@write_logs
def func_test(x, y):
    return sum(x_1**y for x_1 in list(range(x)))


@write_logs
def func_test_2(x, y):
    return sum(x_1**y for x_1 in list(range(x)))


func_test(4555504, 2)
func_test_2(24555, 4)
