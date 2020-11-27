"""
Tuples are list whose values you cannot change once 
you have constructed.

Immutable : Things which you cannot change
mutable : Things which you can change


So tuples are immutable

tuple or ()

# A = ["Apple", "Banana", "HAm"]

A = A[::-1]

money = [75, 100, 2200]


# typecast between a list and a tuple

A = (1, 2, 3, 4, 5)

A = list(A)
A[0] = 10

# we can join two list by using + operator
.
>>> A = [1,2, 3,4,5]
>>> B = [6, 7, 9]

>>> C = A + B
>>> [1, 2 , 3, 4, 5, 6, 7, 9]

A = [1, 2, 34, 5]

B = (1, 2, 3)

A = tuple(A)
A[0] = 10 # you cannot do this 
print(A[0])

"""


"""
problem1;
Given a string S and an integer n repeat each character of 
string S n times

eg
"add" n = 3
"aaadddddd"

"ham" n = 4
"hhhhaaaammmm"

def make_string(s, n):
    res = ""
    for c in s:
        res += c * n
    return res


print(make_string("ABC", 5))


"""

def F(s, n):
    res = list()
    for c in s:
        for x in range(n):
            res.append(c) # ['a','a','a,', 'b','b','b','c','c','c']

    res_str = ""
    for x in res:
        res_str += x

    return res_str # 'aaabbbccc'


"""
given = "Hello people this is me"

output = "me is this people Hello"

["Hello", "people", "this", "is", "me"]

["me", "is", "this", "people", "Hello"]

"""

def split_into_list(words):
    word = ""
    res = list()
    for c in words:
        if c == " ":
            res.append(word)
            word = ""
        else:
            word += c
    res.append(word)
    return res

def join_list_to_str(l):
    ans = ""
    for r in l:
        ans += r + " "
    return ans

res = split_into_list("hey boy this is a class")
res = res[::-1]
print(join_list_to_str(res))



