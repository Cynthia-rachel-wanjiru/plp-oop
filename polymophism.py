class Animal:
    """
    Represents a generic animal.
    """
    def __init__(self, name):
        """
        Initializes an Animal object.

        Args:
            name (str): The name of the animal.
        """
        self.name = name

    def move(self):
        """
        Defines the default move action for an animal.
        This method is meant to be overridden by subclasses.
        """
        print(f"{self.name} moves.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    """
    Represents a dog.
    """
    def __init__(self, name, breed):
        """
        Initializes a Dog object.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
        """
        super().__init__(name)
        self.breed = breed

    def move(self):
        """
        Overrides the move() method for a dog.
        """
        print(f"{self.name} runs.")

    def bark(self):
        print(f"{self.name} barks: Woof!")

    def make_sound(self): #override
        print(f"{self.name} the {self.breed} barks")


class Cat(Animal):
    """
    Represents a cat.
    """
    def __init__(self, name, color):
        """
        Initializes a Cat object.

        Args:
            name (str): The name of the cat.
            color (str): The color of the cat.
        """
        super().__init__(name)
        self.color = color

    def move(self):
        """
        Overrides the move() method for a cat.
        """
        print(f"{self.name} walks.")

    def meow(self):
        print(f"{self.name} meows: Meow!")

    def make_sound(self): #override
        print(f"{self.name} the {self.color} cat meows")


class Vehicle:
    """
    Represents a generic vehicle.
    """
    def __init__(self, model, color):
        """
        Initializes a Vehicle object.

        Args:
            model (str): The model of the vehicle.
            color (str): The color of the vehicle.
        """
        self.model = model
        self.color = color

    def move(self):
        """
        Defines the default move action for a vehicle.
        This method is meant to be overridden by subclasses.
        """
        print(f"The {self.color} {self.model} moves.")


class Car(Vehicle):
    """
    Represents a car.
    """
    def __init__(self, model, color, num_doors):
        """
        Initializes a Car object.

        Args:
            model (str): The model of the car.
            color (str): The color of the car.
            num_doors (int): The number of doors.
        """
        super().__init__(model, color)
        self.num_doors = num_doors

    def move(self):
        """
        Overrides the move() method for a car.
        """
        print(f"The {self.color} {self.model} drives.")


class Plane(Vehicle):
    """
    Represents a plane.
    """
    def __init__(self, model, color, airline):
        """
        Initializes a Plane object.

        Args:
            model (str): The model of the plane.
            color (str): The color of the plane.
            airline (str): The airline the plane belongs to.
        """
        super().__init__(model, color)
        self.airline = airline

    def move(self):
        """
        Overrides the move() method for a plane.
        """
        print(f"The {self.color} {self.model} flies.")



# Example Usage:
if __name__ == "__main__":
    # Create animal objects
    dog1 = Dog("Buddy", "Golden Retriever")
    cat1 = Cat("Whiskers", "Gray")

    # Create vehicle objects
    car1 = Car("Toyota Camry", "Blue", 4)
    plane1 = Plane("Boeing 747", "White", "Kenya Airways")

    # Call the move() method on each object
    dog1.move()  # Output: Buddy runs.
    cat1.move()  # Output: Whiskers walks.
    car1.move()  # Output: The Blue Toyota Camry drives.
    plane1.move()  # Output: The White Boeing 747 flies.

    # Show polymorphism in action with a list
    animals = [dog1, cat1]
    vehicles = [car1, plane1]

    print("\nDemonstrating Polymorphism with Animals:")
    for animal in animals:
        animal.move()  # Calls the appropriate move() method for each animal type
        animal.make_sound()

    print("\nDemonstrating Polymorphism with Vehicles:")
    for vehicle in vehicles:
        vehicle.move()  # Calls the appropriate move() method for each vehicle type
