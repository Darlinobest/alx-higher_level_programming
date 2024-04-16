#!/usr/bin/python3
# 2-square.py
# Darlington K Onwuemebolam
""" Class definition of Square"""


class Square:
    """ Represent the class square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
