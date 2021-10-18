def func_():
    a = 5
    b = a

    def func_func2(*args):
        s = args[0]
        print(b + s)
    return func_func2


print(func_.__code__.co_varnames, len(func_.__code__.co_varnames))
func_()(3)
