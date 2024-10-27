import random
from race import Race
from car import Car

cars = []
for i in range(10):
    reg_number = f"ABC-{i + 1}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))

# Create an 8000 km race called Grand Demolition Derby
race_distance = 8000
race_name = " Ceylon Car Fiesta"
race = Race(race_name, race_distance, cars)

hour = 0
# Simulate the race loop
while not race.race_finished():
    hour += 1
    race.hour_passes()

    # Print status every 10 hours
    if hour % 10 == 0:
        print(f"\n--- Race Status after {hour} hours ---")
        race.print_status()

# Print final status at the end of the race
print("\n--- Final Race Status ---")
race.print_status()