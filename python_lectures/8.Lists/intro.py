# """
# Wheneve we declare or store something in a variable
# the variable is assigned to a unique address
# in ram and the value of the variable is stored at 
# that positition.


# Lists:
# Lists is a type of datastructure
# where all the values are present next to each
# other and it has indexes which starts from 
# 0 and go to the (size of the list - 1)

# in python we denote list with
# [] or list()

# Declare a list:

# fruits = ["Apple", "Banana", "Papaya"]

# Api: (application programming interface) / tools

# 1. To get the size of the list

# len:

# len(fruits) : it will tell you the size of the lists

# 2. Accessing the item of the list

# fruits[1] -> Banana
# fruits[0] -> Apple
# fruits[2] -> Papaya

# fruits[3] -> error

# 3. range(0, 4)
# Slices in arrays

# 4. Negative indexing:
# -6  -5 -4 -3 -2 -1
# 0   1  2  3  4  5 
# [1, 2, 3, 4, 5, 6]

# A[: idx] -> will print from start till idx - 1
# A[idx:] -> will print from idx till end
# A[:] -> will print whole list

# A[0:-1] -> 0 till second last element

# """

# # objects = [
# #     "Apple",
# #     "Banana",
# #     "Papaya",
# #     "Kite",
# #     "WAter",
# #     "Handpump"
# # ]

# # print("length of the list is ", len(objects))

# # print("Element at index 2", objects[2])

# # print(objects[0: len(objects): 2])


# """
# Program to print elements in array
# """

# # way 1
# names = ["Rahul", "Shyam", "Sadaf", "Akash"]

# # for idx in range(0, len(names)):
# #     print("Hello", names[idx])


# # cnt = 1
# # for name in names:
# #     print(cnt, ".", "Hello", name)
# #     cnt += 1


# # for idx in range(0, len(names)):
# #     print(idx + 1, ".", names[idx])

# cnt = 1
# while len(names) > 0:
#     print(cnt, "Hello", names[0])
#     names = names[1:]
#     cnt += 1




"""
1. Hello Rahul
2. Hello Shyam
3. Hello Sadaf
4. Hello Akash
"""

def printpattern(n):
    cnt = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(cnt, end=" ")
            cnt += 1
        print()

user_input = int(input())
printpattern(user_input)