class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute for all Animal objects
    all_animals = []
    kingdom = "Animalia"

    # Initializer with name and species attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species
        # Add the newly created animal to the all_animals list
        Animal.all_animals.append(self)

    # Method to make a generic sound
    def speak(self):
        print("The animal makes a noise.")

    # String representation method
    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"

    @classmethod
    def from_full_name(cls, name, species):
        return cls(name[0], species)

    def print_animal_data(self):
        print(f"ANIMAL INFO \n"
              f"\tNAME: {self.name}\n"
              f"\tSPECIES: {self.species}\n"
              f"\tKINGDOM: {self.kingdom}\n")

    @classmethod
    def get_all_animals(cls):
        return cls.all_animals