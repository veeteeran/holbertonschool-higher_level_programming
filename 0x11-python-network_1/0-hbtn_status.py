#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(url) as response:
        read = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(read)))
        print('\t- content: {}'.format(read))
        print('\t- utf8 content: {}'.format(read.decode("UTF-8")))
