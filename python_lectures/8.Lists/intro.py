"""
Wheneve we declare or store something in a variable
the variable is assigned to a unique address
in ram and the value of the variable is stored at 
that positition.


Lists:
Lists is a type of datastructure
where all the values are present next to each
other and it has indexes which starts from 
0 and go to the (size of the list - 1)

in python we denote list with
[] or list()

Declare a list:

fruits = ["Apple", "Banana", "Papaya"]

Api: (application programming interface) / tools

1. To get the size of the list

len:

len(fruits) : it will tell you the size of the lists

2. Accessing the item of the list

fruits[1] -> Banana
fruits[0] -> Apple
fruits[2] -> Papaya

fruits[3] -> error

3. range(0, 4)
Slices in arrays

"""

objects = [
    "Apple",
    "Banana",
    "Papaya", 
    "Kite",
    "WAter",
    "Handpump"
]

print("length of the list is ", len(objects))

print("Element at index 2", objects[2])

print(objects[0: len(objects): 2])