'''Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
import car'''


car_details = car.make_car('tata', 'hexa', colour='blue', type='toplevel')
print(car_details)

from car import make_car

car_detail = make_car('tata', 'nexon', colour='white', type='manual')
print(car_detail)

from car import make_car as mc

car_making = mc('toyato', 'innovia', colour='white', type='automatic')
print(car_making)

import car as cr

car_making = cr.make_car('hydunai', 'i20', colour='red', type='manual')
print(car_making)

from car import *

car_making = make_car('hydunai', 'verna', colour='white')
print(car_making)
