#!/usr/bin/python3
def search_replace(my_list, search, replace):
    matrix = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            matrix.append(replace)
        else:
            matrix.append(my_list[i])
        i += 1
    return (matrix)
