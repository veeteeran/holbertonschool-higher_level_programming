#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from requests import get

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
