"""
BOOLEAN OPERATORS

operators which will give your 
either True or False

1. EQUALITY OPERATOR / COMPARISON ( == )
=====================================

Schenario 1. 

>>> a = 1
>>> b = 1

>>> a == b -> True

>>> a = 2
>>> b = 1

>>> a == b -> False

=====================================

Schenario 2. 

>>> a = 1
>>> b = 1
>>> c = 2

>>> c == b + a

=====================================

Schenario 3. 

>>> student1 = "rahul"
>>> student2 = "rahul"

>>> student1 == student2 // True


>>> student1 = "rahul"
>>> student2 = "Rahul"

>>> student1 == student2 // False



!= -> opposite of == 
a = 1
b = 2
a != b -> True
a == b -> False


2. GATES (are something which you can put between 2 boolean values)

AND gate -> and
OR gate  -> or
NOT gate -> not


weather = "sunny"
temp = "20"

if weather is sunny and temp is 20

AND : if at its both side the conditions are true then only it will give you true

x and y -> the answer will be true only if x and y both are true.

x    y    x and y
T    T      T
T    F      F
F    T      F
F    F      F

OR : 

x or y -> if any of x or y is true the total result will be True else it will be false

x    y   x or y
T    F     T
F    T     T
T    T     T
F    F     F


NOT:

not x:
x        not x

True     False
False    True



"""

"""

Below program will take user input and will print its remainder . 

"""

print("Hey ! please enter an integer")
no = int(input())

print("The remainder is ", no % 2)

