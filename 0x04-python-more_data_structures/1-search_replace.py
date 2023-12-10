#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for k in my_list:
        if k == search:
            new_list.append(replace)
        else:
            new_list.append(k)
    return new_list
