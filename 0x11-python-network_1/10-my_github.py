#!/usr/bin/python3
"""
 script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    token = sys.argv[2]
    api = " https://api.github.com/user"
    data = {"username": name}
    token = {f"Authorization": f"token {token}"}
    res = requests.get(url=api, params=data, headers=token)
    try:
        print(res.json()['id'])
    except Exception:
        print("None")
