#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element_count = 0
    try:
        for elements in my_list[:x]:
            print("{}".format(elements), end="")
            element_count += 1
        print()
    except Exception as e:
        print(f"Error {e}")
    return element_count
