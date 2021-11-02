from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def get_int(*args):
            result = []
            for arg in args:
                if isinstance(arg, str):
                    if arg.replace(".", "1").isdigit():
                        result.append(int(float(arg)))
                    else:
                        raise TypeError
                elif isinstance(arg, bool):
                    if arg:
                        result.append(1)
                    else:
                        result.append(0)
                elif isinstance(arg, float):
                    result.append(int(arg))
                else:
                    result.append(int(arg))
            return result

        return get_int

    @staticmethod
    def to_str(func):
        @wraps(func)
        def get_str(*args):
            result = " ".join(map(str, args))
            return result

        return get_str

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def get_bool(*args):
            if args:
                return True
            else:
                return False
        return get_bool

    @staticmethod
    def to_float(func):
        @wraps(func)
        def get_float(*args):
            result = []
            for arg in args:
                if isinstance(arg, str):
                    if arg.replace(".", "1").isdigit():
                        result.append(float(arg))
                    else:
                        raise TypeError
                elif isinstance(arg, bool):
                    if arg:
                        result.append(1.0)
                    else:
                        result.append(0.0)
                elif isinstance(arg, int):
                    result.append(float(arg))
                else:
                    result.append(arg)
            return result

        return get_float


@TypeDecorators.to_int
def func_test_int(number):
    return number


@TypeDecorators.to_str
def func_test_str(number):
    return number


@TypeDecorators.to_bool
def func_test_bool(number):
    return number


@TypeDecorators.to_float
def func_test_float(number):
    return number


print(func_test_int(5.6, "55.4", True, 45, "55.7"))
print(func_test_str(56, 24, 68, True))
print(func_test_bool())
print(func_test_bool(45, "ff", True))
print(func_test_float(5.6, "55.4", True, 45, "55"))
print(func_test_float(5.6, "55.4", True, 45))
