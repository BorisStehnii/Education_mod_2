
class Fraction():

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number / other.number

    def __float__(self):
        return self.number


x = Fraction(1/2)
y = Fraction(1/4)

assert x + y == float(Fraction(3/4)), "Error"
assert x - y == float(Fraction(1/4)), "Error"
assert x * y == float(Fraction(1/8)), "Error"
assert x / y == float(Fraction(4/2)), "Error"
