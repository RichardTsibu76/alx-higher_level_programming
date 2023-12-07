#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        evaluate = list()
        for number_for_loop in my_list:
            if number_for_loop % 2 == 0:
                evaluate.append(True)
            else:
                evaluate.append(False)
        return evaluate
