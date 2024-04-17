#!/usr/bin/python3
# 6-square.py
# Darlington K Onwuemebolam

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__seize

    @size.setter
    def size(self, value):
        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
       
    """ prints a square with # symbol """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.position[1] > 0:
            print("\n" * self.position[1], end="")

        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
