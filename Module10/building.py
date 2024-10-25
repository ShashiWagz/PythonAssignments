from Module10.elevator import Elevator


class Building:
    def __init__(self, top, bottom, num):
        self.top = top
        self.bottom = bottom
        self.num_of_elevators = num
        self.elevators = []
        for i in range(self.num_of_elevators):
            self.elevators.append(Elevator(self.top, self.bottom))

    def run_elevators(self, num, destination_floor):
        if num < 1 or num >self.num_of_elevators:
            print("Invalid Elevator Number")
            return
        print(f"Moving Elevators {num}")
        self.elevators[num-1].got_to_floor(destination_floor)


