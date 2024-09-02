import random
input_user=int(input("How many dice to roll?..."))
total_rolls=0

for _ in range(input_user):
    rolls=random.randint(1,6)
    total_rolls+=rolls
    print(rolls)


print("Sum of the numbers is :  ", total_rolls)
