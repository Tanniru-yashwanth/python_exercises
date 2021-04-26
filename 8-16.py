import car
car_details = car.make_car('tata', 'hexa', colour='blue', type='toplevel')
print(car_details)


from car import make_car
car_detail = make_car('tata', 'nexon', colour='white', type='manual')
print(car_detail)


from car import make_car as mc
car_making = mc('toyato', 'innovia', colour='white', type='automatic')
print(car_making)


import car as cr
car_making = cr.make_car('hydunai','i20', colour='red', type='manual')
print(car_making)


from car import *
car_making = make_car('hydunai', 'verna', colour='white')
print(car_making)