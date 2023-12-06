#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        stor_len = len(my_list)
        if idx < 0 or idx >= stor_len:
            return my_list
        new_list = []
        for lable_integer in range(0, stor_len):
            if lable_integer == idx:
                new_list.append(element)
            else:
                new_list.append(my_list[lable_integer])
        return new_list
