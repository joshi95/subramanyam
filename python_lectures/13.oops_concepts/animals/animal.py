class Animal:
    def __init__(self, name, no_of_legs):
        """
        Animal: constructor for the class Animal
        """
        print("Animal constructor is called.")

        self.name = name
        self.no_of_legs = no_of_legs

    
    def eat(self):
        """
        eat: takes no argument and will make the 
        animal eat food.
        """
        print(f"{self.name} is eating")

    def walk(self):
        """
        walk: animal will walk
        """
        print(f"{self.name} is walking")