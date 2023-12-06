#!/usr/bin/python3
def element_at(my_list, idx):
     num = len(my_list)
    if idx < 0 or idx > (num - 1):
        return None
    for number in range(0, num):
        if number == idx:
            return (my_list[idx])
