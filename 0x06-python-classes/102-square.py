#!/usr/bin/python3
# 102-square.py
# Darlington K Onwuemebolam
""" Class definition of Square """


class Square:
    """ Represent the class square """
    def __init__(self, size=0):
        """ Initialize the square with the given size """
        self.size = size

    @property
    def size(self):
        """ Getter method for the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
    def __eq__(self, other):
        """ Compares two squares for area equality """
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """ Compares to squares for inequality based o their area"""
        return not self.__eq__(other)

    def __gt__(self, other):
        """ Compare two squares based on their areas """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """ Compare two squares based on their areas """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """ Compare two squares based on their areas """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """ Compare two squares based on their areas """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
