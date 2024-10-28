import random
from car import Car
from tabulate import tabulate

cars = []
for i in range(10):
    reg_number=f"ABC - {i+1}"
    maximum_speed= random.randint(100, 200)
    cars.append(Car(reg_number,maximum_speed))

race= True
hour=0
while race:
    hour+=1
    for car in cars:
        changed_speed=random.randint(-10,15)
        car.accelerate(changed_speed)

        car.drive(1)

        if car.travelled_distance >= 10000:
            print(f"Car {car.registration_number} wins!")
            race=False
            break

results = []
for car in cars:
    results.append([car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance])

print("Results of the Race")
print(tabulate(results, headers=["Registration", "Max Speed", "Current Speed", "Travelled Distance"], tablefmt="grid"))