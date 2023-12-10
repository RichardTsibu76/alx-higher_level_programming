#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = list()
    for key_in_value in a_dictionary.keys():
        keys_list.append(key_in_value)
    for integer in keys_list:
        if a_dictionary[i] == value:
            del a_dictionary[integer]
    return a_dictionary
