"""
Student: represents a student.
__init__: this is pronunced as dunder init / constructor
"""


class Student:
    def __init__(self):
        """
        attrs:
        name: denotes the name of the student.
        age: denotes the age of the student.
        birth_year: denotes the birth year of the student.
        """

        self.name = "Shyam"
        self.age = 10
        self.birth_year = 1997

    def read(self):
        """
        read: read is a method of student class.
        """
        print(f"student {self.name} is reading !! ")

    def write(self):
        """
        write: write is a method of student class.
        """
        print(f"student {self.name} is writing !! ")
