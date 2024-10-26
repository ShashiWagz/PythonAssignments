from car import Car

car1 = Car("ABC-123", 142)

print(f'''
Registration number : {car1.registration_number} ,
Maximum_Speed : {car1.maximum_speed} Current_Speed : {car1.current_speed}
Current_Speed : {car1.current_speed}
Travelled_Distance : {car1.travelled_distance}
'''
      )

car1.accelerate(30)
print(f'Current Speed after accelerate +30 km/h: {car1.current_speed}')

car1.accelerate(70)
print(f'Current Speed after accelerate +70 km/h: {car1.current_speed}')

car1.accelerate(50)
print(f'Current Speed after accelerate +50 km/h: {car1.current_speed}')


car1.accelerate(-200)
print(f'Current Speed after emergency break: {car1.current_speed}')

