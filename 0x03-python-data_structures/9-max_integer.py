#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maximum = None
        for number in my_list:
            if maximum is None or number > maximum:
                maximum = number
        return maximum
