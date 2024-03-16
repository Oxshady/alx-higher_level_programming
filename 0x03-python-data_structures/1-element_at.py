#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if lenght <= idx or lenght < 0:
        return None
    else:
        return my_list[idx]
