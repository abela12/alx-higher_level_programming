#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    Defines a square by private attribute size,
    and instantiation with optional size:
    def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """
        private instance attribute
        parameters
        ------------------
        size : integer else TypeError
        if size less than 0, raise value error
        """
        self.__size = size
        try:
            assert type(size) == int
        except:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
