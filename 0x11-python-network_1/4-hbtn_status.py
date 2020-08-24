#!/usr/bin/python3
from requests import get
"""Fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
