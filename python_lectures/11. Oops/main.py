from student import Student # Importing


if __name__ == "__main__":

    # Student Kunal
    kunal = Student("Kunal Chopra", 23, 1998)
    print(f"name: {kunal.name} age : {kunal.age} birth_year: {kunal.birth_year}")
    kunal.read()
    kunal.write()

    kunal.give_mcq("tuples")

    # Student Abhijit
    abhijit = Student("Abhijit Sharma", 24, 2001)
    print(abhijit.name)
    abhijit.read()

    abhijit.give_mcq("oops")

    subject, marks = abhijit.get_marks()
    print(f"abhijit got {marks} in {subject}")

