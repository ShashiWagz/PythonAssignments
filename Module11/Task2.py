import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, amount):
        self.current_speed += amount
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours=1):
        self.traveled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

# Main program for Part 2
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Set speed for both cars
electric_car.accelerate(150)
gasoline_car.accelerate(140)

# Drive both cars for three hours
electric_car.drive(3)
gasoline_car.drive(3)

# Print out the kilometer counters
print("\nElectric Car Information:")
print(f"Registration Number: {electric_car.registration_number}")
print(f"Traveled Distance: {electric_car.traveled_distance} km")

print("\nGasoline Car Information:")
print(f"Registration Number: {gasoline_car.registration_number}")
print(f"Traveled Distance: {gasoline_car.traveled_distance} km")
