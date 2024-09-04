
city_list=[]

for i in range(5):
    city=str(input(f"Enter a city name {i+1}:"))
    city_list.append(city)

print("")

print("The cities you entered are .....")
for city in city_list:
    print(city)

