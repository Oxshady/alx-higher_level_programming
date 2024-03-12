#!/usr/bin/python3
for x in range(10):
    for z in range(10):
        if z == 9 and x == 9:
            print(f"{x:d}{z:d}")
        else:
            print(f"{x:d}{z:d}", end=", ")
