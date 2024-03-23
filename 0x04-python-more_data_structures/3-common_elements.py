#!/usr/bin/python3
def common_elements(set_1, set_2):
    same_element = set()
    for i in set_1:
        if i in set_2:
            same_element.add(i)
    return same_element
