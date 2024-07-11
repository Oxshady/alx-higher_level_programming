#!/bin/python3
"""
The Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges
Only 17% of applicants for a backend position at
Holberton finished this task in less than 15 minutes
"""

import sys
import requests
import json
if __name__ == "__main__":
    api = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    key = "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"
    header = {"Authorization": f"token {key}"}
    res = requests.get(url=api, headers=header)
    res = res.json()
    for i in range(10):
        sha = res[i].get('sha')
        name = res[i].get('commit').get('author').get('name')
        print(f"{sha}: {name}")
