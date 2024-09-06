import random

def dice_roll(sides):
    return random.randint(1, sides)

def main():
    sides=int(input("Enter the number of sides: "))

    rolls=0
    while rolls != sides:
        rolls =dice_roll(sides)
        print(f"The rolled :{rolls}")

if __name__ == '__main__':
    main()

