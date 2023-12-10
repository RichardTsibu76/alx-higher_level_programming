#!/usr/bin/python3
def uniq_add(my_list=[]):
    compare_list = my_list.copy()
    for i in my_list:
        idx = 1
        for k in compare_list:
            if i == k and idx == 1:
                idx += 1
                continue
            elif i == k:
                compare_list.remove(k)
    add = 0
    for j in compare_list:
        add += j
    return add
