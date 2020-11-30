"""
Student: represents a student.
__init__: this is pronunced as dunder init / constructor
"""

import random

class Student:
    def __init__(self, name, age, birth_year):
        """
        attrs:
        name: denotes the name of the student.
        age: denotes the age of the student.
        birth_year: denotes the birth year of the student.
        """

        self.name = name
        self.age = age
        self.birth_year = birth_year

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

    def give_mcq(self, topic):
        """
        give_mcq: 
        args:
        topic: denotes the topic of the mcq.
        """
        print(f"student {self.name} gave mcq of topic {topic}")


    def get_marks(self):
        """
        get_marks: returns a string denoting the marks text.
        """
        subjects = ["maths", "geography", "sociollogy"]
        random_subject = subjects[random.randint(0, len(subjects) - 1)]
        return random_subject, random.randint(1, 100)
