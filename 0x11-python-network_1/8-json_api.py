#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data_dict = {}
    if len(argv) < 2:
        data_dict = {'q': ''}
    else:
        data_dict = {'q': argv[1]}

    r = post(url, data=data_dict)
    try:
        if r.json() == {}:
            print('No result')
        else:
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
    except:
        print('Not a valid JSON')
