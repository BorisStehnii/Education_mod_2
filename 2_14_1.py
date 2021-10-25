class Animals():

    def say(self):
        raise NotImplementedError("Error: no 'say' method")


class Dog(Animals):

    def say(self):
        print("woof-woof")


class Cat(Animals):

    def say(self):
        print("miu-miu")


def play_say(class_):
    class_.say()


cat = Cat()
dog = Dog()
play_say(cat)
play_say(dog)

