#!/usr/bin/python3
"""
This module defines a Student class with filtered JSON output.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: The dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            res = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    res[k] = v
            return res
        return self.__dict__
