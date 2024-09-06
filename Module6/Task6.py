import math

def pizza_sqm(diameter_cm, price_euro):
    radius_in_meters=diameter_cm/100/2
    area=radius_in_meters**2*math.pi
    return price_euro/area

pizza1_price=float(input(f"Enter your first choice pizza price (euro):  "))
size_pizza1=int(input("Enter your first choice pizza size (cm) : "))
pizza2_price=float(input(f"Enter your second choice pizza price (euro):  "))
size_pizza2=int(input("Enter your second choice pizza size: (cm) "))

pizza_1=pizza_sqm(size_pizza1,pizza1_price)
pizza_2=pizza_sqm(size_pizza2,pizza2_price)

if pizza_1>pizza_2:
    print('pizza 1 is better than pizza 2')
else:
    print('pizza 2 is better than pizza 1')


