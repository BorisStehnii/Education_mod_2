class Person():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.surname} and I’m {self.age} years old")


massage_1 = "Name: "
massage_2 = "Surname: "
massage_3 = "Age: "


if __name__ == '__main__':
    name_ = input(massage_1)
    surname_ = input(massage_2)
    age_ = input(massage_3)
    person = Person(name_, surname_, age_)
    person.talk()
