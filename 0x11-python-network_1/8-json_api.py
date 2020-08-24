#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    r = get(argv[1])
    if r.status_code >= 400:
            print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
