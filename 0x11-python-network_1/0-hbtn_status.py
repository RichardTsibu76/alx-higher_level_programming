#!/usr/bin/python3
# A python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    alx = response.read().decode('utf-8')
    print('Body response:')
    print("\t- type:", type(alx))
    print("\t- content:", alx)
    print("\t- utf8 content:", alx)
