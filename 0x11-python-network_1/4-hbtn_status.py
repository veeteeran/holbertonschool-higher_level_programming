#!/usr/bin/python3
from urllib.request import urlopen, Request
"""Fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(url) as response:
        read = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(read.decode("UTF-8"))))
        print('\t- content: {}'.format(read.decode("UTF-8")))
