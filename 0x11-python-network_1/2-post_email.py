#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = {"email": email}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url=url, data=data)
with urllib.request.urlopen(req) as res:
    print(res.read().decode('utf-8'))
