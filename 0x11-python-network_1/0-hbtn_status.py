#!/usr/bin/python3
# A python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

with urllib.request.urlopen(request) as response:

    body = response.read()

    print("Body response:")

    print("\t- type: {}".format(type(body)))

    print("\t- content: {}".format(body))

    print("\t- utf8 content: {}".format(body.decode("utf-8")))
