#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    result = 0
    for i in my_list:
        if i not in unique_list:
            result += i
            unique_list.add(i)
    return result
