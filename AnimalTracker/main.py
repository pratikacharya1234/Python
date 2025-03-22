from animal import Animal
from dog import Dog

# Create initial animal objects
jefry = Animal("Jefry", "Bhotey")
tiger = Animal("Tiger", "Tibetian Mastiff")
lona = Animal("Lona", "German Shepherd")

if __name__ == "__main__":
    # Original test code
    print("Individual animal data:")
    jefry.print_animal_data()
    tiger.print_animal_data()
    lona.print_animal_data()

    print("\nTesting speak method:")
    jefry.speak()
    tiger.speak()
    lona.speak()

    print("\nString representation:")
    print(jefry)
    print(tiger)
    print(lona)

    # New main block requirements
    # Create an instance of the Animal class
    lion = Animal("Leo", "Panthera leo")
    
    # Print the Animal instance
    print("\nNew Animal instance:")
    print(lion)
    
    # Call the method to make a generic animal sound
    lion.speak()

    # Create an instance of the Dog class
    rex = Dog("Rex", "Canis lupus familiaris", "German Shepherd")
    
    # Print the Dog instance
    print("\nNew Dog instance:")
    print(rex)
    
    # Call the method to make the dog-specific sound
    rex.speak()

    # Print out all the animals
    print("\nAll animals in the system:")
    all_animals = Animal.get_all_animals()
    for animal in all_animals:
        print(animal)