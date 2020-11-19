"""
This code will show you how to do typecasting

Whenever you want a specific type to be converted
to another type we say it as typecasting

it is simple ;)

just wrap data in int() or str() or float()

>>> a = "5"
a = int("5")
"""


print("Typecasting from str to int")

a = "5"
print("before: ", type(a))

a = int("5")
print("after:", type(a))



print("Typecasting from int to str")

a = 5
print("before: ", type(a))

a = str(a)
print("after:", type(a))
