"""
This sections we will study about if / else statement

>>> if(<boolean_condition>):
        print("HI")
        a = 3
        b = 4
        print(a + b) 

if inside an if is nesting.

"""

a = 4
if (a % 2 == 0 or a >= 4):

    if (a % 2 == 0):
        print("The no is even")
    
        if (a == 8):
            print("The no is 8")

    if (a >= 4):
        print("The no is greater than or equal to 4")

print("program completed")
