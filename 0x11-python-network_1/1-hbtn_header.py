#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.info()['X-Request-Id'])
