#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        tup = (0, None)
        return tup
    else:
        tup = (lenght, sentence[0])
        return tup
