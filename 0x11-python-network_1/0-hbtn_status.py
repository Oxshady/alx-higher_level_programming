#!/usr/bin/python3
"""
 Python script that fetches
 https://alx-intranet.hbtn.io/status
"""

import urllib
import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as res:
    ress = res.read()
    x = f"Body response:\n\t- type: {type(ress)}\n\t"
    print(x + f"- content: {ress}\n\t- utf8 content: {ress.decode()}")
