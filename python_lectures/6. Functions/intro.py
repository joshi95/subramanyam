"""
Functions: are some constructs available in 
programming languages by which we can reduce duplicacy
in code and make our code easy to understand.

Here we will be wrapping our code in small small bodies
which we would be invoking / calling.


def <a_name_of_a_function>():

Once a function is created you can call its code by
<name_of_function>()

=============================

example 1

def greet():
    print("Hello")
    print("Welcome to this class ")  

# Greeting

# greet() # calling a function

print("press some thing ")
print("abcdd")


greet() 

print("adfsdf")
print("fdsfsdf")


greet()

=============================
Example 2: 

def cubeTillN():
    N = 5
    sum = 0
    for i in range(1, N + 1):
        sum += i ** 3
    print(sum)

# cube_till_n() #call


=============================


example 3


def greet():
    print("Please enter some no: ", end="")
    N = int(input())
    print("Good Morning!!")
    for x in range(0, N):
        print(x)

def walk():
    print("Walking!!")

def sleep():
    print("Sleeping")

walk()
sleep()
greet()
sleep()
walk()



"""

# sum of cube of numbers from 1 to N.

