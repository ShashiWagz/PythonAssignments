import random


def dice():
    return random.randint(1,6)

def main():
    rolls=0
    while rolls !=6:
        rolls=dice()
        print(f"The rolled result is : {rolls}")


if __name__ == '__main__':
    main()

