class Vehicle():

    def cover_distance(self, distance):
        raise NotImplementedError("Error: no 'cover_distance' method")

    def set_avg_speed_ph(self, speed):
        self._avg_speed_ph = speed

    def __lt__(self, other):
        return self._avg_speed_ph < other._avg_speed_ph

    def __eq__(self, other):
        return self._avg_speed_ph == other._avg_speed_ph


class Bike(Vehicle):

    def __init__(self, avg_speed_ph=25):
         self._avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        time = round(distance / self._avg_speed_ph, 2)
        print(f"I am bike. It take me about {time} hours")


class Car(Vehicle):

    def __init__(self, avg_speed_ph=90):
        self._avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        time = round(distance / self._avg_speed_ph, 2)
        print(f"I am care. It take me about {time} hours")


class Plane(Vehicle):

    def __init__(self, avg_speed_ph=400):
        self._avg_speed_ph = avg_speed_ph

    def cover_distance(self, distance):
        time = round(distance / self._avg_speed_ph, 2)
        print(f"I am plane. It take me about {time} hours")


bike = Bike()
car = Car()
plane = Plane()
for veh in [bike, car, plane]:
    veh.cover_distance(60)

for veh, speed in zip([bike, car, plane], [30, 120, 500]):
    veh.set_avg_speed_ph(speed)

for veh in [bike, car, plane]:
    veh.cover_distance(60)

print(car > bike)
print(bike > plane)
print(bike == bike)
