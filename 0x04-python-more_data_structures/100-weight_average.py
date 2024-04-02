#!/ust/bin/python3
def weight_average(my_list=[]):
    sum_of_weight = 0
    total_weight = 0
    if not my_list:
        return 0
    for score, weight in my_list:
        sum_of_weight += score * weight
        total_weight += weight
        if total_weight == 0:
            return 0
    return sum_of_weight / total_weight
