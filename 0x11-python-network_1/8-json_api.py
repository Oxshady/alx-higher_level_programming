#!/usr/bin/python3
"""
 script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys

if __name__ == "__main__":
    q = {"q": ""}
    try:
        value = sys.argv[1]
        q = {"q": value}
    except IndexError:
        pass
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url=url, data=q)
    try:
        res = res.json()
        if res:
            print(f"[{res['id']}] {res['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
