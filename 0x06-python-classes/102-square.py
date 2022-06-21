#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    Private instance attribute size
    public instance method
    """
    def __init__(self, size=0):
        """private instance attribute
        parameters
        -------------------------
        size : integer else TypeError
        if size less than 0, raise value error
        """
        self.__size = size

    @property
    def size(self):
        """
        to retrieve private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set private instance attribute
        """
        self.__size = value
        try:
            assert type(value) == int
        except:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        returns the current square area
        """
        area = self.__size ** 2
        return area

    def __lt__(self, other):
        """check for less than"""
        if self.__size ** 2 < other.__size ** 2:
            return True
        return False

    def __le__(self, other):
        """check for <="""
        if self.__size ** 2 <= other.__size ** 2:
            return True
        return False

    def __eq__(self, other):
        """check for =="""
        if self.__size ** 2 == other.__size ** 2:
            return True
        return False

    def __ne__(self, other):
        """check for !="""
        if self.__size ** 2 != other.__size ** 2:
            return True
        return False

    def __gt__(self, other):
        """check for >"""
        if self.__size ** 2 > other.__size ** 2:
            return True
        return False

    def __ge__(self, other):
        """check for >="""
        if self.__size ** 2 >= other.__size ** 2:
            return True
        return False
