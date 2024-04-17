#!/usr/bin/python3
# 5-Square.py
# Darlington K Onwuemebolam
""" Definition of a class """


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
        """ prints a square with # symbol """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
