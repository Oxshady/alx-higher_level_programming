#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set()
    for i in set_1:
        found = False
        for ii in set_2:
            if i == ii:
                found = True
                break
        if not found:
            res.add(i)
    for i in set_2:
        found = False
        for ii in set_1:
            if i == ii:
                found = True
                break
        if not found:
            res.add(i)
    return (res)
