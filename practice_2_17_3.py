"""
Реализуйте класс-итератор, который будет генерировать числа Фибоначчи.
Каждое следующее число равно сумме двух последних.
"""


class FiboNums:

    def __init__(self, num):
        self.num = num
        self.ind_ = 0
        self.first_ = 0
        self.next_ = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind_ < self.num:
            res, self.first_, self.next_ = self.first_, self.next_, self.next_ + self.first_
            self.ind_ += 1
            return res
        raise StopIteration


def fibo_nums(num):
    first_ = 0
    next_ = 1
    for _ in range(num):
        yield first_
        first_, next_ = next_, next_ + first_


fib = FiboNums(15)
for el in fib:
    print(el, end=" ")

print("")

print(list(fibo_nums(15)))
