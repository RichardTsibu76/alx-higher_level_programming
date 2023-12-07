#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        length = 0
        charat1 = None
    else:
        length = len(sentence)
        charat1 = sentence[0]
    return length, charat1
