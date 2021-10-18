from functools import reduce


def make_calc(oper):

    def mult(*args):
        print("*")
        mult_ = reduce(lambda x, y: x*y, args)
        return mult_

    def minus(*args):
        print("-")
        minus_ = reduce(lambda x, y: x-y, args)
        return minus_

    def plus(*args):
        print("+")
        sum_ = reduce(lambda x, y: x+y, args)
        return sum_

    dict_ = {
        "+": plus,
        "-": minus,
        "*": mult
    }
    return dict_[oper]


print(make_calc("*")(1, 2, 3, 4))
