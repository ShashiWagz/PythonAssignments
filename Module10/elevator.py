from tkinter.messagebox import RETRY


class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def got_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor")
            return
        while target_floor > self.current_floor:
            self.floor_up()


        while target_floor < self.current_floor:
            self.floor_down()

        #up or down?
        #call floor up & down

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(self.current_floor)
        #go up 1 floor
#       print current floor
    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(self.current_floor)
        #go down 1 floor
        #print current floor