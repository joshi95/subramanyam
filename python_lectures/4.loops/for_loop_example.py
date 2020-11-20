"""
Loops are constructs in programming language which helps you 
to repeat some section of code. 

There are 2 types of loop.

1. While 

2. For 

For Loop:

for i in range(5):
    print(i)


Question 1: Print all the even no in between [0 - 100]

Question 2: Print even no in reverse [100 - 1]

Question 3: Given n from user print from [ 1 - n ]
is divisible by 3 print FIZZ 
if any of them is divisible by 5
if divisible by both  FIZZ_FUZZ
else: print normal 


no = 15
1 2 FIZZ 4 FUZZ FIZZ 7 8 FIZZ FUZZ 11 FIZZ 13 14 FIZZ_FUZZ
"""

user_input = int(input())

for i in range(1, user_input + 1):
    if i % 5 == 0 and i % 3 == 0:
        print(i, "FIZZ_FUZZ")
    elif i % 5 == 0:
        print(i, "FUZZ")
    elif i % 3 == 0:
        print(i, "FIZZ")
    else:
        print(i)
        
pir