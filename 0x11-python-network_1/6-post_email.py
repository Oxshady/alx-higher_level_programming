#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL withthe email as a parameter,
and finally displays the body of the response
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    res = requests.post(url=url, data=email)
    print(res.text)
