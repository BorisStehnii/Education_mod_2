from typing import List, Union, Any, Iterable


class Vehicle:

    def cover_distance(self, distance: int):
        raise NotImplementedError("Abstract method should be implemented")

    def set_avg_speed_ph(self, speed: int) -> None:
        self._avg_speed_ph: int = speed

    def _cover_distance_formula(self, distance: int, rnd: int =2) -> float:
        return round(distance / self._avg_speed_ph, rnd)

    def __repr__(self):
        return f"{self.__class__.__name__}>>{self._avg_speed_ph}"

    def __lt__(self, vehicle) -> bool:
        return self._avg_speed_ph < vehicle._avg_speed_ph

    def __eq__(self, vehicle) -> bool:
        return self._avg_speed_ph == vehicle._avg_speed_ph


class Bike(Vehicle):

    def __init__(self, avg_speed_ph: int = 25) -> None:
        self._avg_speed_ph: int = avg_speed_ph

    def cover_distance(self, distance: int) -> None:
        print(f"I am a bike. It takes me about {self._cover_distance_formula(distance)} hours")

    # def __repr__(self):
    #     return f"{self.__class__.__name__}>>{self._avg_speed_ph}"


class Car(Vehicle):

    def __init__(self, avg_speed_ph: int = 80):
        self._avg_speed_ph: int = avg_speed_ph

    def cover_distance(self, distance: int) -> None:
        print(f"I am a car. It takes me about {self._cover_distance_formula(distance)} hours")


class Plane(Vehicle):

    def __init__(self, avg_speed_ph: int = 300) -> None:
        self._avg_speed_ph: int = avg_speed_ph

    def cover_distance(self, distance: int) -> None:
        print(f"I am a plane. It takes me about {self._cover_distance_formula(distance)} hours")


def filter_the_fastest(vehicles: List[Union[Plane, Bike, Car]]) -> Vehicle:
    fast: Vehicle = vehicles[0]
    for ele in vehicles:
        if ele > fast:
            fast = ele
    return fast


bike_1 = Bike(65)
bike_2 = Bike(105)
car_1 = Car(50)
car_2 = Car(40)
plane_1 = Plane(100)
print(filter_the_fastest(vehicles=[bike_1, bike_2, car_2, car_1, plane_1]))

