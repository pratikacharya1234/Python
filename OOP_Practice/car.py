from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, make, model, year, num_door):
        super().__init__(make, model, year)
        self.door = num_door

        #possible to add a list of features
    def __str__(self):
        return super().__str__() + f", Doors:{self.num_door}"