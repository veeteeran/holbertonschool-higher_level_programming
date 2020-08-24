#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses
   the Github API to display your id
"""
from requests import get, post
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    r = get(url)
    commits = r.json()
    counter = 0
    for commit in commits:
        if counter == 10:
            break
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
        counter += 1
