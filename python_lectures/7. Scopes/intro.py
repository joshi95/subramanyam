"""
Scopes:
===========================

Example 1:
def ABC():
    sum = 10
    for x in range(10):
        sum = 0
    print(sum)

ABC()

===========================

Example 2:

sum = 0 # global scope
def ABC():
    sum = 5
    print("inner sum", sum)


ABC()

print("outer sum", sum)


Global scope: Any variable outside a function is
called to be in global scope.

Local scope: Any thing inside a function is called 
local scope.

When we are accessing the sum inside the function
we will get the sum from the local scope

else outside the function we will get from global scope.

Example 3

sum = 0 # global scope

def ABC():
    sum = 10
    for i in range(1,10):
        sum += 5
    print("inner sum", sum)

sum = 10
print("outer sum", sum)
ABC()



"""

