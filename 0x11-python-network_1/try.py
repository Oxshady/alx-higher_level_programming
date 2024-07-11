#!/usr/bin/python3
# """
#  Python script that fetches
#  https://alx-intranet.hbtn.io/status
# """

# import urllib
# import urllib.request

# req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
# with urllib.request.urlopen(req) as res:
#     ress = res.read()
#     x= res.getheaders()
#     print(x)
#     print(res.headers)
import sys
print(sys.argv[0])