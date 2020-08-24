#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    try:
        email = {'email': argv[2]}
        r = post(argv[1], data=email)
        print(r.text)
    except:
        pass
