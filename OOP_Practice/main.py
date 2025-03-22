from vehicle import Vehicle
from car import Car

black_car = Vehicle("Tesla","Model S",2003)
red_car =Vehicle("Toyota","Corolla",2005)

all_vehicle = Vehicle.get_all_vechiles()
for car in [black_car,red_car]:
    make,model,year = car
    new_car = Vehicle(make,model,year)