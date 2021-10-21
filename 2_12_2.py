class Dog():
    age_factor = 7

    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
        print(self.age_dog * self.age_factor)


while True:
    age_dogs = input("Enter age dog: ")
    if age_dogs.isdigit():
        dog = Dog(int(age_dogs))
        dog.human_age()
        break
    else:
        continue
