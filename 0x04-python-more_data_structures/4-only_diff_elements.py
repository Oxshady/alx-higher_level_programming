#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set({})
    stat = 0
    for i in set_1:
        for ii in set_2:
            if i != ii:
                stat = 1
            else:
                stat = 0
        if stat == 1:
            res.add(i)
    for i in set_2:
        for ii in set_1:
            if i != ii:
                stat = 1
            else:
                stat = 0
        if stat == 1:
            res.add(i)
    return (res)
