#!/usr/bin/python3
"""
cript that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url=url)
    try:
        x_request = res.headers['X-Request-Id']
    except:
        exit(-1)    
    if x_request:
        print(x_request)
