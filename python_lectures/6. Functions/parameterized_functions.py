# """
# A function can take inputs also which are called
# parameters to the functions. 

# The parameters are the types of python only.
# eg int, float, str, list etc..

# And a function can return some data which also are of
# types.
# eg int, float, str, list etc...

# to supply input to the function / parameters to the 
# function we add the variables which we want as input
# inside the parenthesis.

# and to get the output we use the keywork return then
# the thing we want to return for eg
# in the below case sum of no1 and no2 


# Returns:

# Whenever some function returns a value it is your 
# duty to capture it in some variable.

# ===========================

# Example 1
# # This function will take two no's as input
# # and will give output as their sum.
# def addTwoNumbers(no1, no2):
#     sum = no1 + no2
#     return sum


# x = int(input())
# y = int(input())
# ans = addTwoNumbers(x, y)
# print(ans)


# """

# """
# This function will take a no as input
# and will output True if the no is even else
# output False
# """
# def isNoEven(no):
#     if no % 2 == 0:
#         print("no is even")
#         return True
#     else:
#         print("no is odd")
#         return False

# res = isNoEven(105)
# print(res)



# """
# n = 5
# *
# * *
# * * *
# * * * *
# * * * * *

# n = 3
# *
# * *
# * * *

# n = 4
# *
# * *
# * * *
# * * * *


# whenver you multiply a string with an integer
# you will repeat it that many times.


# """

def printPatternWithForLoop(rows):
    for row in range(1, rows + 1):
        for noOfStars in range(row):
            print("*", end=" ")
        print()

def printPatternWithWhileLoop(rows):
    row = 1
    while row <= rows:
        noOfStars = 0
        while noOfStars < row:
            print("*", end=" ")
            noOfStars += 1
        print()
        row += 1

def printWithMultiplication(rows):
    for row in range(1, rows + 1):
        print("* " * row)


print("Please enter no of rows", end="")
noOfRows = int(input())
print("With for loop")
printPatternWithForLoop(noOfRows)

print("With while loop")
printPatternWithWhileLoop(noOfRows)

print("With multipliation")
printWithMultiplication(noOfRows)


def Test(no1, no2):
    for x in range(no1, no2):
            if no1 == 5:
                return 5
            if no2 == 2:
                return no1 + no2
    return no1 * no2



print(Test(1, 2))
print(Test(2, 3))
