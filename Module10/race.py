import random
from car import Car
from tabulate import tabulate

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            # Generate random speed change between -10 and +15
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            # Car drives for 1 hour at the current speed
            car.drive(1)

    def print_status(self):
        print(f"\nRace Name: {self.name}")
        # Format and print the current status of each car
        headers = ["Registration", "Max Speed", "Current Speed", "Travelled Distance"]
        data = [
            [
                car.registration_number,
                car.maximum_speed,
                car.current_speed,
                car.travelled_distance
            ] for car in self.cars
        ]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def race_finished(self):
        # Check if any car has completed the race distance
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False