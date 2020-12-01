from animals.animal import Animal


class Dog(Animal):
    def __init__(self, name, no_of_legs, has_tail):
        """
        Dog: constructor for the dog class. Here it 
        is calling the parents class constructor so that the attributes of the 
        parent can be initialized.
        """
        print("Dog constructor is called")
        super().__init__(name, no_of_legs)
        self.has_tail = has_tail

    def bark(self):
        """
        bark: bark is a method by which our dog will bark. Since dog is a
        type of animal so it will have all the attributes of animal. ie self.name is 
        accessible in Dog class.
        """
        print(f"{self.name} is barking")


