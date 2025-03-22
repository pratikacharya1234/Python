class Vehicle:

    all_vehicle = []
     
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


        Vehicle.all_vechiles.append(self)



    def d__str__(self):
        return f"Year:{self.year}, Make:{self.make}, Model:{self.model}"
    

    @classmethod
    def get_all_vechiles():
        return Vehicle.all_vechiles