class Car:

    @classmethod
    def create_new_car(cls, model, color):
        new_car = cls()
        new_car._model = model
        new_car._color = color
        return new_car

    @property
    def car_model(new_car):
        return new_car._model

    @car_model.setter
    def car_model(new_car, new_model):
        if not isinstance(new_model, str):
            raise TypeError
        new_car._model = new_model

    @car_model.deleter
    def car_model(new_car,):
        new_car._model = None

    @property
    def car_color(new_car):
        return new_car._color

    @car_color.setter
    def car_color(new_car, new_color):
        if not isinstance(new_color, str):
            raise TypeError
        new_car._color = new_color

    @car_color.deleter
    def car_color(new_car):
        new_car._color = None


bmw = Car.create_new_car("bmw", "black")
opel = Car.create_new_car("opel", "grey")
bmw.car_model = "M5"
print(bmw.car_model)
del bmw.car_model
print(bmw.car_model)
bmw.car_color = "black"
print(bmw.car_color)
del bmw.car_color
print(bmw.car_color)
