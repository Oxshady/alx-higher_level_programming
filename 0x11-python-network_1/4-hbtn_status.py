#!/usr/bin/python3
"""
script that fetches
https://alx-intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    x = f"Body response:\n\t- type: {type(res.text)}\n\t"
    print(x + f"- content: {res.text}")
