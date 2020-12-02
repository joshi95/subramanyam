"""
If any method name or attribute name
starts with an underscore then you should not use
it outside a class. 

if you will use it program will not break or no error 
will occur, but in python community if you use 
_ attribute or method outside the class then it is 
called bad practice.

if _ is in front of attribute or method then
we call private
else we call it public.



OOPS Principles:

1. Inheritance: parent children relationship
children has all the attributes and methods of the parent
and you can do method overridding in this.

2. Encapsulation: Anything inside a class should not be
directly accessible outside the class.

3. Abstraction: Hidding the details of a method 
or a class.

4. Polymorphism: Poly means many so polymorphoism means
your code can take different forms.


"""

class Animal:
    def __init__(self):
        print("Animal constructor is called")

    def walk(self):
        print("Animal is walking")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor is called")

    def bark(self):
        print("Dog is barking")

    def walk(self):
        super().walk()
        print("Dog is walking.")


class Bank:
    def __init__(self):
        self._amount = 0
        self._increase_amount()

    def _increase_amount(self):
        self._amount += 1


if __name__ == "__main__":
    b = Bank()
    b._increase_amount()

