#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
        return []
    for x in range(0, list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
