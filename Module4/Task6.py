import random

num_of_random_points=int(input("Enter the number of random points to generate: "))
n=0
iterator = 0

while iterator<num_of_random_points:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x ** 2 + y ** 2 < 1:
        n=n+1
    iterator +=1
print( 4 * n / num_of_random_points)