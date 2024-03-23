#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    general_set = set()
    for i in set_2:
        if i not in set_1:
            general_set.add(i)
    for i in set_1:
        if i not in set_2:
            general_set.add(i)
    return general_set
