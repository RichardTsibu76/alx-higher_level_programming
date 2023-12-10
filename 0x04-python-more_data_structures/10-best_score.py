#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maximum = None
        for key, val in a_dictionary.items():
            if maximum is None or a_dictionary[key] > maximum:
                maximum = a_dictionary[key]
                highest = key
        return highest
