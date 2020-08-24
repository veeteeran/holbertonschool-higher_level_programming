#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the
    body of the response
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    try:
        r = get(argv[1])
        print(r.text)
    except:
        if r.status_code >= 400:
            print('Error code: {}'.format(r.status_code))
