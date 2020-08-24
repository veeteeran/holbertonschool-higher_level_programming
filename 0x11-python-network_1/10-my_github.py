#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses
   the Github API to display your id
"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    token = argv[2]
    r = get(url, auth=(user, token))

    try:
        id = (r.json()['id'])
        print(id)
    except KeyError:
        print('None')
