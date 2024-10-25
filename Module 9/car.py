class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = reg_number
        self.maximum_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, Change_of_speed):
        self.current_speed = self.current_speed + Change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0


    def drive(self, num_of_hours=0):
        distance = self.current_speed * num_of_hours
        self.travelled_distance += distance

