import time


class Person():

    planet = "Earth"

    def __init__(self):
        self.cats = []

    def get_a_cat(self, new_cat):
         self.cats.append(new_cat)

    def call_cats(self):
        for cat in self.cats:
            if (time.time()-cat.time_save) > 20:
                cat.is_hungry = "No"
            elif (time.time()-cat.time_save) > 10:
                cat.is_hungry = True
            print(f"{cat.name}, color-{cat.color}\n is hungry {cat.is_hungry}")
            if cat.is_hungry == "Died":
                print("Cat died")
                self.cats.remove(cat)
            elif cat.is_hungry:
                cat.say_meow()

    def feed_cats(self):
        for cat in self.cats:
            if cat.is_hungry:
                cat.is_hungry = False
                cat.time_save = time.time()

    def feed_a_cat_by_name(self, name):
        name = name.lower()
        for cat in self.cats:
            if cat.name == name:
                cat.is_hungry = False
                cat.time_save = time.time()


class Cat():

    def __init__(self, name, age, color="colorful"):
        self.name = name
        self.age = age
        self.color = color
        self.is_hungry = True
        self.time_save = time.time()

    def say_meow(self):
        print(f"{self.name} <<Meow!!!>>")


massage_1 = "add cat: A, check cats: C, feed cats: F, feed cat: N, get out: E>> "
massage_2 = "Name cat: "
massage_3 = "Age cat: "
massage_4 = "Color cat: "
massage_5 = "Get out of the house(Е/n): "


def commands(person):
    command = input(massage_1)
    if command.lower() == "a":
        name_cat = input(massage_2)
        age_cat = input(massage_3)
        color_cat = input(massage_4)
        cat_1 = Cat(name_cat, age_cat, color_cat)
        person.get_a_cat(cat_1)
    elif command.lower() == "c":
        person.call_cats()
    elif command.lower() == "f":
        person.feed_cats()
    elif command.lower() == "n":
        name_cat = input(massage_2)
        person.feed_a_cat_by_name(name_cat)
    else:
        person.call_cats()
        person.feed_cats()
        command_1 = input(massage_5)
        if command_1.lower() == "e":
            exit(0)


if __name__ == '__main__':
    boris = Person()
    while True:
        commands(boris)
