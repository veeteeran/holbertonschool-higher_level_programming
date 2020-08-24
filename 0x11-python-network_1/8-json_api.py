#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        arg = argv[1]
    except IndexError:
        print('No result')
        quit()

    data_dict = {'q': arg}
    r = post(url, data=data_dict)
    try:
        if r.json() == {}:
            print('No result')
        print('[{}] {}'.format(r.json()['id'], r.json()['name']))
    except:
        print('Not a valid JSON')
