from student import Student # Importing


if __name__ == "__main__":
    kunal = Student() # we are making an object of type Student

    print(kunal.age)
    print(kunal.name)
    print(kunal.birth_year)

    kunal.read()
    kunal.write()
