#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num = len(my_list)
    if idx < 0 or idx >= num:
        return (my_list)
    for i in range(0, num):
        if i == idx:
            my_list[i] = element
            return (my_list)
