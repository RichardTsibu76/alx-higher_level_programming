#!/usr/bin/python3
# A python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    alx = response.read()
