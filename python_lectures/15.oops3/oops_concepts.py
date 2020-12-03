# # """
# # Inheritance:

# # Encapsulation:

# # Abstraction:

# # Polymorphism


# # """

# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self._amount = 0

#     def add_amount(self, x):
#         self._amount += x

#     def get_amount(self):
#         return self._amount

# class HDFC(Bank):
#     def __init__(self):
#         name = "HDFC"
#         super().__init__(name)

# if __name__ == "__main__":
#     bank = HDFC()
#     bank.add_amount(100)
#     print(bank.get_amount())


# """
# Polymorphism: Same type of objects but different behaviour
# """


# class Shape:
#     def __init__(self, name):
#         self.name = name


# class Square(Shape):
#     def __init__(self, name, side):
#         super().__init__(name)
#         self.side = side

#     def area(self):
#         return self.side * self.side


# class Rectangle(Shape):
#     def __init__(self, name, x, y):
#         super().__init__(name)
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y


# if __name__ == "__main__":
#     square = Square("square", 6)
#     print(f"The area of {square.name} is {square.area()}")

#     rectangle = Rectangle("rectangle", 5, 3)
#     print(f"The area of {rectangle.name} is {rectangle.area()}")

from cod import COD
from credit_card import CreditCard

if __name__ == "__main__":
    cod = COD(1000)
    cod.make_payment()

    cc = CreditCard(1000)
    cc.make_payment()