"""
A dictionary is a datastructure which 
has key and a value

A dictonary is represented via {} or dict()

eg:
{
    key1: value1,
    key2: value2,
    key3: value3,
}

now keys: can only be (str or int or float)
and values: can be any data type 
eg(int, str, list, tuple, float)

# property 1:
The keys in a dictionary are always unique

# property 2:
To access a particular key value in a dictionary
we will use 
state_capital_dict["Haryana"]

# to put a new key in a dictionary or update a dictionary 

A = [0, 1, 2, 4,]
A[3] = 8

>>> state_capital_dict["ABC"] = [1,2,3]

the above command will update the key ABC to the new value or if not present
will add the key with the value


# property 3

delete a key in a dictionary by using 
dict.pop('key_name')

# property 4

to get all the keys of dictionary you use
.keys()

to get all the values of a dictionary you use 
.values()


#property 5
len -> for a dictionary will give you the total no of keys in the dictionary.

#property 6
looping


state_capital_dict = {
    "Delhi": "Delhi",
    "Haryana": "Chandigardh",
    "Punjab": "Chandigardh",
    "MP": "Bhopal",
    "Cities": [1, 2, 3, 4],
    "delhi": "Punjab",
}

"Cities" in state_capital_dict

account = {
    1: "Rohan",
    2: "Ram",
}

time_table = {
    "monday": ["english", "maths"],
    "tuesday": ["abc"]
}

for key in state_capital_dict.keys():
    print("for key", key, "value is ", state_capital_dict[key])

for key, value in state_capital_dict.items():
    print(key, value)


"""

# in

# 33 in [1,3, 4, 5, 6,10]


# finding the max value

# # [4, 5, 6, 1, 2, 3, 4]
# A = [4, 5, 6, 1, 2, 3, 4]
# max_val = A[0]

# for i in range(1, len(A)):
#     if A[i] > max_val:
#         max_val = A[i]

# print(max_val)


# how we create a dictionary


# Q1. Given a list with values [1, 2, 1, 1, 1, 2, 3, 4, 5 , 5]
# Tell me the frequency of each value eg 1 -> 4, 2 -> 2, 3 - > 1, 4 - > 1, 5 -> 2


parties = ["Congress", "BJP", "BJP", "BJP", "AAP", "AAP"]

party_dict = dict()

for party in parties:
    if party in party_dict:
        party_dict[party] += 1
    else:
        party_dict[party] = 1


{
    "Congress": 1,
    "BJP": 3,
    "AAP": 2,
}



winning_party = ""
max_votes = 0

for key in party_dict.keys():
    if max_votes < party_dict[key]:
        max_votes = party_dict[key]
        winning_party = key


# 
s = "a boy is good."

l = ["a", "and", "is", "good"]


res = ""
for word in l:
    if word == "and":
        res += ","
    else:
        res += word
