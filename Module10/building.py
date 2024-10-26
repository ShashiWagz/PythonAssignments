from Module10.elevator import Elevator


class Building:
    def __init__(self, bottom,top, num):
        self.top = top
        self.bottom = bottom
        self.num_of_elevators = num
        self.elevators = []
        for i in range(self.num_of_elevators):
            self.elevators.append(Elevator(self.bottom, self.top))

    def run_elevators(self, num, destination_floor):
        if num < 1 or num >self.num_of_elevators:
            print("Invalid Elevator Number")
            return
        print(f"Moving Elevators {num}")
        self.elevators[num-1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm triggered! Moving all elevators to the bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f'''
                  Elevator {i + 1} moving to bottom floor:''')
            elevator.go_to_floor(self.bottom)
