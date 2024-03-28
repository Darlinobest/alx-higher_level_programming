#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary == None:
        return None
    else:
        values = a_dictionary.values()
        max_value = max(values)
        keys = a_dictionary.keys()
        for keys in a_dictionary:
            if a_dictionary[keys] == max_value:
                return keys
