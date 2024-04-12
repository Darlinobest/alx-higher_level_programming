#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            print("Not an integer")
            return False
     except Exception as e:
         print(f"Error {e}")
         return False
