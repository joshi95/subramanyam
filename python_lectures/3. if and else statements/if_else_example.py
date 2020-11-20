"""

Example to demonstrate if and else statement.

"""

first_name = "desh"
last_name = "raj"

if first_name == "desh":
    if last_name == "raj":
        print("desh raj is from subramanyam batch")
    else:
        if last_name == "Raj":
            print("Seems like you have done a typo")
            
        print("desh is not from subramanyam batch")
else:
    print("the student name is unknown")
