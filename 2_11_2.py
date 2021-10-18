def func_2():
    def func_2_1(*args_2):
        sum_1 = sum(args_2)
        return sum_1
    return func_2_1


print(func_2()(3, 4))
